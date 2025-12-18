"""
Лаборатори 05: System Testing - Airport Connection
Choice-based testing methodology
"""

from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List, Tuple
import unittest


@dataclass
class Flight:
    """Нислэгийн мэдээлэл"""
    flight_number: str
    departure_airport: str
    arrival_airport: str
    departure_time: datetime
    arrival_time: datetime
    is_international: bool


def valid_connection(flight_a: Flight, flight_b: Flight) -> bool:
    """
    Хоёр нислэгийн холболт хүчинтэй эсэхийг шалгах.
    
    Шаардлагууд:
    1. FlightA-н буух газар FlightB-н хөөрөх газартай ижил байх
    2. Холболтын хугацаа 30 минут - 4 цаг байх
    3. Олон улсаас дотоод руу шилжихэд 2+ цаг хэрэгтэй
    
    Returns:
        True хэрэв холболт хүчинтэй бол
    """
    # Rule 1: Airport match
    if flight_a.arrival_airport != flight_b.departure_airport:
        return False
    
    # Rule 2: Connection time (30 min - 4 hours)
    connection_time = flight_b.departure_time - flight_a.arrival_time
    min_connection = timedelta(minutes=30)
    max_connection = timedelta(hours=4)
    
    if connection_time < min_connection or connection_time > max_connection:
        return False
    
    # Rule 3: International to Domestic requires 2+ hours
    if flight_a.is_international and not flight_b.is_international:
        if connection_time < timedelta(hours=2):
            return False
    
    return True


# ============ CHOICE-BASED TEST CASES ============

class TestAirportConnection(unittest.TestCase):
    """
    Choice-based testing for validConnection function.
    
    Choices:
    - Airport Match: Same, Different
    - Connection Time: TooShort (<30min), Valid (30min-4hr), TooLong (>4hr), Negative
    - Flight Types: Dom-Dom, Dom-Int, Int-Dom, Int-Int
    """
    
    def setUp(self):
        """Base time for tests"""
        self.base_time = datetime(2024, 6, 15, 10, 0)  # 10:00 AM
    
    def create_flight(self, number: str, dep_airport: str, arr_airport: str,
                      dep_offset_min: int, duration_min: int, 
                      is_international: bool = False) -> Flight:
        """Helper to create flight"""
        dep_time = self.base_time + timedelta(minutes=dep_offset_min)
        arr_time = dep_time + timedelta(minutes=duration_min)
        return Flight(
            flight_number=number,
            departure_airport=dep_airport,
            arrival_airport=arr_airport,
            departure_time=dep_time,
            arrival_time=arr_time,
            is_international=is_international
        )
    
    # ============ TC01-TC03: Airport Match Tests ============
    
    def test_TC01_same_airport_valid_time_dom_dom(self):
        """TC01: Same airport, valid time (60min), Domestic-Domestic -> Valid"""
        flight_a = self.create_flight("MN101", "UBN", "ICN", 0, 180, False)
        flight_b = self.create_flight("MN201", "ICN", "NRT", 240, 120, False)
        # Connection: 60 min (180 + 60 = 240)
        
        self.assertTrue(valid_connection(flight_a, flight_b))
    
    def test_TC02_different_airport_invalid(self):
        """TC02: Different airport -> Invalid (regardless of other factors)"""
        flight_a = self.create_flight("MN101", "UBN", "ICN", 0, 180, False)
        flight_b = self.create_flight("MN201", "NRT", "HKG", 240, 120, False)  # Different!
        
        self.assertFalse(valid_connection(flight_a, flight_b))
    
    # ============ TC04-TC07: Connection Time Tests ============
    
    def test_TC04_time_too_short(self):
        """TC04: Connection time too short (<30 min) -> Invalid"""
        flight_a = self.create_flight("MN101", "UBN", "ICN", 0, 180, False)
        flight_b = self.create_flight("MN201", "ICN", "NRT", 195, 120, False)
        # Connection: 15 min (195 - 180 = 15)
        
        self.assertFalse(valid_connection(flight_a, flight_b))
    
    def test_TC05_time_valid_minimum(self):
        """TC05: Connection time at minimum (30 min) -> Valid"""
        flight_a = self.create_flight("MN101", "UBN", "ICN", 0, 180, False)
        flight_b = self.create_flight("MN201", "ICN", "NRT", 210, 120, False)
        # Connection: 30 min (210 - 180 = 30)
        
        self.assertTrue(valid_connection(flight_a, flight_b))
    
    def test_TC06_time_valid_maximum(self):
        """TC06: Connection time at maximum (4 hours) -> Valid"""
        flight_a = self.create_flight("MN101", "UBN", "ICN", 0, 180, False)
        flight_b = self.create_flight("MN201", "ICN", "NRT", 420, 120, False)
        # Connection: 240 min = 4 hours (420 - 180 = 240)
        
        self.assertTrue(valid_connection(flight_a, flight_b))
    
    def test_TC07_time_too_long(self):
        """TC07: Connection time too long (>4 hours) -> Invalid"""
        flight_a = self.create_flight("MN101", "UBN", "ICN", 0, 180, False)
        flight_b = self.create_flight("MN201", "ICN", "NRT", 500, 120, False)
        # Connection: 320 min > 4 hours (500 - 180 = 320)
        
        self.assertFalse(valid_connection(flight_a, flight_b))
    
    def test_TC08_time_negative(self):
        """TC08: Negative connection time (FlightB departs before FlightA arrives) -> Invalid"""
        flight_a = self.create_flight("MN101", "UBN", "ICN", 0, 180, False)
        flight_b = self.create_flight("MN201", "ICN", "NRT", 100, 120, False)
        # Connection: -80 min (100 - 180 = -80)
        
        self.assertFalse(valid_connection(flight_a, flight_b))
    
    # ============ TC09-TC12: Flight Type Tests ============
    
    def test_TC09_dom_dom_valid(self):
        """TC09: Domestic to Domestic, valid time -> Valid"""
        flight_a = self.create_flight("MN101", "UBN", "ICN", 0, 180, False)
        flight_b = self.create_flight("MN201", "ICN", "NRT", 240, 120, False)
        
        self.assertTrue(valid_connection(flight_a, flight_b))
    
    def test_TC10_dom_int_valid(self):
        """TC10: Domestic to International, valid time -> Valid"""
        flight_a = self.create_flight("MN101", "UBN", "ICN", 0, 180, False)
        flight_b = self.create_flight("MN201", "ICN", "NRT", 240, 120, True)
        
        self.assertTrue(valid_connection(flight_a, flight_b))
    
    def test_TC11_int_dom_short_time_invalid(self):
        """TC11: International to Domestic, short time (60 min) -> Invalid (needs 2+ hours)"""
        flight_a = self.create_flight("MN101", "UBN", "ICN", 0, 180, True)  # International
        flight_b = self.create_flight("MN201", "ICN", "NRT", 240, 120, False)  # Domestic
        # Connection: 60 min < 2 hours required
        
        self.assertFalse(valid_connection(flight_a, flight_b))
    
    def test_TC12_int_dom_long_time_valid(self):
        """TC12: International to Domestic, long time (120 min) -> Valid"""
        flight_a = self.create_flight("MN101", "UBN", "ICN", 0, 180, True)  # International
        flight_b = self.create_flight("MN201", "ICN", "NRT", 300, 120, False)  # Domestic
        # Connection: 120 min = 2 hours (exactly minimum)
        
        self.assertTrue(valid_connection(flight_a, flight_b))
    
    def test_TC13_int_int_valid(self):
        """TC13: International to International, valid time -> Valid"""
        flight_a = self.create_flight("MN101", "UBN", "ICN", 0, 180, True)
        flight_b = self.create_flight("MN201", "ICN", "NRT", 240, 120, True)
        
        self.assertTrue(valid_connection(flight_a, flight_b))


# ============ TEST SUMMARY ============

def print_test_summary():
    """Print test case summary table"""
    print("""
╔══════╦═══════════════╦═════════════════╦═══════════╦══════════╗
║  TC  ║ Airport Match ║ Connection Time ║   Types   ║ Expected ║
╠══════╬═══════════════╬═════════════════╬═══════════╬══════════╣
║ TC01 ║ Same          ║ Valid (60min)   ║ Dom-Dom   ║ Valid    ║
║ TC02 ║ Different     ║ Valid (60min)   ║ Dom-Dom   ║ Invalid  ║
║ TC04 ║ Same          ║ TooShort (15m)  ║ Dom-Dom   ║ Invalid  ║
║ TC05 ║ Same          ║ Valid (30min)   ║ Dom-Dom   ║ Valid    ║
║ TC06 ║ Same          ║ Valid (4hr)     ║ Dom-Dom   ║ Valid    ║
║ TC07 ║ Same          ║ TooLong (5hr)   ║ Dom-Dom   ║ Invalid  ║
║ TC08 ║ Same          ║ Negative        ║ Dom-Dom   ║ Invalid  ║
║ TC09 ║ Same          ║ Valid (60min)   ║ Dom-Dom   ║ Valid    ║
║ TC10 ║ Same          ║ Valid (60min)   ║ Dom-Int   ║ Valid    ║
║ TC11 ║ Same          ║ Valid (60min)   ║ Int-Dom   ║ Invalid  ║
║ TC12 ║ Same          ║ Valid (120min)  ║ Int-Dom   ║ Valid    ║
║ TC13 ║ Same          ║ Valid (60min)   ║ Int-Int   ║ Valid    ║
╚══════╩═══════════════╩═════════════════╩═══════════╩══════════╝
    """)


if __name__ == "__main__":
    print_test_summary()
    print("\nRunning tests...\n")
    unittest.main(verbosity=2)
