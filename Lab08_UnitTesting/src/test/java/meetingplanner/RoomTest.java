package meetingplanner;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;
import static org.junit.jupiter.api.Assertions.*;

/**
 * Лаборатори 08: Unit Testing - Meeting Planner
 * RoomTest - Room классын тестүүд
 */
class RoomTest {
    
    private Room room;
    private Meeting meeting1;
    private Meeting meeting2;
    
    @BeforeEach
    void setUp() {
        room = new Room("Conference Room A");
        meeting1 = new Meeting(9, 10, "Morning Standup");
        meeting2 = new Meeting(14, 15, "Afternoon Review");
    }
    
    @Nested
    @DisplayName("Constructor Tests")
    class ConstructorTests {
        
        @Test
        @DisplayName("Room name is set correctly")
        void testRoomName() {
            assertEquals("Conference Room A", room.getName());
        }
        
        @Test
        @DisplayName("New room has no meetings")
        void testNewRoomEmpty() {
            assertEquals(0, room.getMeetingCount());
            assertTrue(room.getMeetings().isEmpty());
        }
    }
    
    @Nested
    @DisplayName("addMeeting Tests")
    class AddMeetingTests {
        
        @Test
        @DisplayName("Add meeting to empty room succeeds")
        void testAddMeetingToEmptyRoom() {
            assertTrue(room.addMeeting(meeting1));
            assertEquals(1, room.getMeetingCount());
        }
        
        @Test
        @DisplayName("Add multiple non-overlapping meetings")
        void testAddMultipleMeetings() {
            assertTrue(room.addMeeting(meeting1));
            assertTrue(room.addMeeting(meeting2));
            assertEquals(2, room.getMeetingCount());
        }
        
        @Test
        @DisplayName("Cannot add overlapping meeting")
        void testCannotAddOverlappingMeeting() {
            Meeting first = new Meeting(9, 11, "Long Meeting");
            Meeting overlapping = new Meeting(10, 12, "Overlapping");
            
            assertTrue(room.addMeeting(first));
            assertFalse(room.addMeeting(overlapping));
            assertEquals(1, room.getMeetingCount());
        }
        
        @Test
        @DisplayName("Meeting room is set after adding")
        void testMeetingRoomSet() {
            room.addMeeting(meeting1);
            assertEquals(room, meeting1.getRoom());
        }
        
        @Test
        @DisplayName("BUG-3: Adding null meeting throws NullPointerException")
        void testBug3_AddNullMeeting() {
            assertThrows(NullPointerException.class, () -> {
                room.addMeeting(null);
            }, "BUG-3: No null check - throws NPE");
        }
    }
    
    @Nested
    @DisplayName("getMeeting Tests")
    class GetMeetingTests {
        
        @Test
        @DisplayName("Get meeting by valid index")
        void testGetMeetingValidIndex() {
            room.addMeeting(meeting1);
            room.addMeeting(meeting2);
            assertEquals(meeting1, room.getMeeting(0));
            assertEquals(meeting2, room.getMeeting(1));
        }
        
        @Test
        @DisplayName("BUG-4: Get meeting with invalid index")
        void testBug4_GetMeetingInvalidIndex() {
            assertThrows(IndexOutOfBoundsException.class, () -> {
                room.getMeeting(0);
            }, "BUG-4: No index bounds validation");
        }
        
        @Test
        @DisplayName("BUG-4: Negative index throws exception")
        void testBug4_NegativeIndex() {
            room.addMeeting(meeting1);
            assertThrows(IndexOutOfBoundsException.class, () -> {
                room.getMeeting(-1);
            });
        }
    }
    
    @Nested
    @DisplayName("removeMeeting Tests")
    class RemoveMeetingTests {
        
        @Test
        @DisplayName("Remove existing meeting")
        void testRemoveExistingMeeting() {
            room.addMeeting(meeting1);
            room.addMeeting(meeting2);
            room.removeMeeting(meeting1);
            assertEquals(1, room.getMeetingCount());
        }
        
        @Test
        @DisplayName("BUG-5: Remove non-existent meeting silently fails")
        void testBug5_RemoveNonExistentMeeting() {
            Meeting notInRoom = new Meeting(20, 21, "Not Added");
            int sizeBefore = room.getMeetingCount();
            room.removeMeeting(notInRoom);
            assertEquals(sizeBefore, room.getMeetingCount(),
                "BUG-5: removeMeeting silently fails");
        }
    }
    
    @Nested
    @DisplayName("isAvailable Tests")
    class IsAvailableTests {
        
        @Test
        @DisplayName("Empty room is always available")
        void testEmptyRoomAvailable() {
            assertTrue(room.isAvailable(9, 17));
        }
        
        @Test
        @DisplayName("Room not available during meeting")
        void testNotAvailableDuringMeeting() {
            room.addMeeting(meeting1);
            assertFalse(room.isAvailable(9, 10));
        }
        
        @Test
        @DisplayName("Room available outside meeting times")
        void testAvailableOutsideMeetings() {
            room.addMeeting(meeting1);
            assertTrue(room.isAvailable(10, 11));
            assertTrue(room.isAvailable(8, 9));
        }
    }
    
    @Test
    @DisplayName("getMeetings returns copy of list")
    void testGetMeetingsReturnsCopy() {
        room.addMeeting(meeting1);
        var meetings = room.getMeetings();
        meetings.clear();
        assertEquals(1, room.getMeetingCount());
    }
    
    @Test
    @DisplayName("clearMeetings removes all meetings")
    void testClearMeetings() {
        room.addMeeting(meeting1);
        room.addMeeting(meeting2);
        room.clearMeetings();
        assertEquals(0, room.getMeetingCount());
    }
}
