"""
Лаборатори 12: FSM Testing - Elevator System
Төгсгөлөг Төлөвийн Машин (Finite State Machine)
"""

from enum import Enum, auto
from typing import List, Optional
import unittest


class ElevatorState(Enum):
    """Лифтний төлөвүүд"""
    IDLE = auto()           # Сул, зогссон
    MOVING_UP = auto()      # Дээшээ явж байна
    MOVING_DOWN = auto()    # Доошоо явж байна
    DOOR_OPEN = auto()      # Хаалга нээлттэй


class Floor(Enum):
    """Давхарууд"""
    BASEMENT = 0
    FLOOR_1 = 1
    FLOOR_2 = 2


class Elevator:
    """
    Лифтний хяналтын систем
    
    Safety Properties:
    P1: Хаалга нээлттэй үед лифт хөдлөхгүй
    P2: Лифт зөвхөн зогссон үедээ хаалгаа нээнэ
    P3: Нэг удаад зөвхөн нэг чиглэлд явна
    """
    
    def __init__(self):
        self.state = ElevatorState.IDLE
        self.current_floor = Floor.FLOOR_1
        self.target_floor: Optional[Floor] = None
        self.door_open = False
        self.requests: List[Floor] = []
    
    def request_floor(self, floor: Floor) -> bool:
        """
        Давхар руу явах хүсэлт
        
        P1: Хаалга нээлттэй үед хүсэлт хүлээн авахгүй
        """
        # P1: Safety check
        if self.state == ElevatorState.DOOR_OPEN:
            print(f"Cannot move: Door is open (P1)")
            return False
        
        if floor == self.current_floor:
            self._open_door()
            return True
        
        self.target_floor = floor
        
        if floor.value > self.current_floor.value:
            self.state = ElevatorState.MOVING_UP
            print(f"Moving UP to {floor.name}")
        else:
            self.state = ElevatorState.MOVING_DOWN
            print(f"Moving DOWN to {floor.name}")
        
        return True
    
    def arrive_at_floor(self, floor: Floor):
        """Давхар дээр ирэх"""
        self.current_floor = floor
        
        if floor == self.target_floor:
            self._open_door()
        else:
            self.state = ElevatorState.IDLE
            print(f"Passed {floor.name}")
    
    def _open_door(self):
        """Хаалга нээх (P2: зөвхөн зогссон үед)"""
        if self.state in [ElevatorState.MOVING_UP, ElevatorState.MOVING_DOWN]:
            raise RuntimeError("P2 Violation: Cannot open door while moving!")
        
        self.state = ElevatorState.DOOR_OPEN
        self.door_open = True
        self.target_floor = None
        print(f"Door opened at {self.current_floor.name}")
    
    def close_door(self):
        """Хаалга хаах"""
        if self.state == ElevatorState.DOOR_OPEN:
            self.door_open = False
            self.state = ElevatorState.IDLE
            print("Door closed")
    
    def door_timeout(self):
        """Хаалга автоматаар хаагдах"""
        self.close_door()
    
    def get_state(self) -> ElevatorState:
        return self.state
    
    def get_current_floor(self) -> Floor:
        return self.current_floor


# ============ FSM STATE TRANSITIONS ============

FSM_DIAGRAM = """
╔══════════════════════════════════════════════════════════════════════╗
║                    ELEVATOR FSM DIAGRAM                               ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                       ║
║    ┌─────────────────────────────────────────────────────────┐       ║
║    │                                                         │       ║
║    │   ┌─────────┐   request_above    ┌───────────┐         │       ║
║    │   │         │ ─────────────────> │           │         │       ║
║    │   │  IDLE   │                    │ MOVING_UP │ ←───┐   │       ║
║    │   │         │ <───────────────── │           │     │   │       ║
║    │   └─────────┘   arrived          └───────────┘  moving │       ║
║    │        │                               │               │       ║
║    │        │ request_below                 │ arrived_target║       ║
║    │        ▼                               ▼               │       ║
║    │   ┌───────────┐                  ┌───────────┐         │       ║
║    │   │           │                  │           │         │       ║
║    │   │MOVING_DOWN│                  │ DOOR_OPEN │         │       ║
║    │   │           │ ────────────────>│           │         │       ║
║    │   └───────────┘  arrived_target  └───────────┘         │       ║
║    │        │                               │               │       ║
║    │        └───────────────────────────────┼───────────────┘       ║
║    │                   arrived              │ timeout               ║
║    │                                        ▼                       ║
║    │                                   ┌─────────┐                  ║
║    └──────────────────────────────────>│  IDLE   │                  ║
║                                        └─────────┘                  ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
"""

TRANSITIONS_TABLE = """
╔═══════════════╦═════════════════════╦═══════════════╦═════════════════╗
║  From State   ║       Event         ║   To State    ║     Action      ║
╠═══════════════╬═════════════════════╬═══════════════╬═════════════════╣
║ IDLE          ║ request_above       ║ MOVING_UP     ║ start motor     ║
║ IDLE          ║ request_below       ║ MOVING_DOWN   ║ start motor     ║
║ IDLE          ║ request_same        ║ DOOR_OPEN     ║ open door       ║
║ MOVING_UP     ║ arrived_target      ║ DOOR_OPEN     ║ stop, open door ║
║ MOVING_UP     ║ arrived_other       ║ IDLE          ║ stop motor      ║
║ MOVING_DOWN   ║ arrived_target      ║ DOOR_OPEN     ║ stop, open door ║
║ MOVING_DOWN   ║ arrived_other       ║ IDLE          ║ stop motor      ║
║ DOOR_OPEN     ║ timeout             ║ IDLE          ║ close door      ║
║ DOOR_OPEN     ║ request_any         ║ DOOR_OPEN     ║ none (P1)       ║
╚═══════════════╩═════════════════════╩═══════════════╩═════════════════╝
"""


# ============ STATE-BASED TEST CASES ============

class TestElevatorFSM(unittest.TestCase):
    """Elevator FSM тестүүд"""
    
    def setUp(self):
        self.elevator = Elevator()
    
    # State Coverage Tests
    def test_TC01_idle_to_moving_up(self):
        """TC01: IDLE -> request(Floor2) -> MOVING_UP"""
        self.assertEqual(self.elevator.get_state(), ElevatorState.IDLE)
        self.elevator.request_floor(Floor.FLOOR_2)
        self.assertEqual(self.elevator.get_state(), ElevatorState.MOVING_UP)
    
    def test_TC02_idle_to_moving_down(self):
        """TC02: IDLE -> request(Basement) -> MOVING_DOWN"""
        self.elevator.request_floor(Floor.BASEMENT)
        self.assertEqual(self.elevator.get_state(), ElevatorState.MOVING_DOWN)
    
    def test_TC03_moving_up_to_door_open(self):
        """TC03: MOVING_UP -> arrived_target -> DOOR_OPEN"""
        self.elevator.request_floor(Floor.FLOOR_2)
        self.elevator.arrive_at_floor(Floor.FLOOR_2)
        self.assertEqual(self.elevator.get_state(), ElevatorState.DOOR_OPEN)
    
    def test_TC04_door_open_stays_on_request_P1(self):
        """TC04: DOOR_OPEN -> request -> DOOR_OPEN (P1: cannot move)"""
        self.elevator.request_floor(Floor.FLOOR_1)  # Opens door (same floor)
        self.assertEqual(self.elevator.get_state(), ElevatorState.DOOR_OPEN)
        
        result = self.elevator.request_floor(Floor.FLOOR_2)
        self.assertFalse(result)  # P1: Cannot move with door open
        self.assertEqual(self.elevator.get_state(), ElevatorState.DOOR_OPEN)
    
    def test_TC05_door_open_to_idle_timeout(self):
        """TC05: DOOR_OPEN -> timeout -> IDLE"""
        self.elevator.request_floor(Floor.FLOOR_1)
        self.assertEqual(self.elevator.get_state(), ElevatorState.DOOR_OPEN)
        
        self.elevator.door_timeout()
        self.assertEqual(self.elevator.get_state(), ElevatorState.IDLE)
    
    def test_TC06_same_floor_opens_door(self):
        """TC06: Floor 1 -> request(Floor1) -> DOOR_OPEN"""
        self.elevator.request_floor(Floor.FLOOR_1)
        self.assertEqual(self.elevator.get_state(), ElevatorState.DOOR_OPEN)
    
    # Safety Property Tests
    def test_P1_no_movement_with_door_open(self):
        """P1: Хаалга нээлттэй үед хөдлөхгүй"""
        self.elevator.request_floor(Floor.FLOOR_1)  # Opens door
        self.assertTrue(self.elevator.door_open)
        
        result = self.elevator.request_floor(Floor.FLOOR_2)
        self.assertFalse(result)
        self.assertEqual(self.elevator.current_floor, Floor.FLOOR_1)
    
    def test_P2_door_opens_only_when_stopped(self):
        """P2: Зөвхөн зогссон үед хаалга нээгдэнэ"""
        self.elevator.request_floor(Floor.FLOOR_2)
        self.assertEqual(self.elevator.get_state(), ElevatorState.MOVING_UP)
        
        # Should not be able to open door while moving
        self.assertFalse(self.elevator.door_open)


if __name__ == "__main__":
    print("=" * 70)
    print("Lab 12: FSM Testing - Elevator System")
    print("=" * 70)
    print(FSM_DIAGRAM)
    print(TRANSITIONS_TABLE)
    print("\nRunning State-Based Tests...")
    print("=" * 70)
    
    unittest.main(verbosity=2)
