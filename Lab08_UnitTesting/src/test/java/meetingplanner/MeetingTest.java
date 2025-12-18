package meetingplanner;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;
import static org.junit.jupiter.api.Assertions.*;

/**
 * Лаборатори 08: Unit Testing - Meeting Planner
 * MeetingTest - Meeting классын тестүүд
 */
class MeetingTest {
    
    private Meeting meeting1;
    private Meeting meeting2;
    
    @BeforeEach
    void setUp() {
        meeting1 = new Meeting(9, 10, "Daily Standup");
        meeting2 = new Meeting(10, 11, "Sprint Planning");
    }
    
    // ============ CONSTRUCTOR TESTS ============
    
    @Nested
    @DisplayName("Constructor Tests")
    class ConstructorTests {
        
        @Test
        @DisplayName("Constructor sets values correctly")
        void testConstructorSetsValues() {
            Meeting meeting = new Meeting(14, 15, "Team Meeting");
            
            assertEquals(14, meeting.getStartTime());
            assertEquals(15, meeting.getEndTime());
            assertEquals("Team Meeting", meeting.getDescription());
            assertNull(meeting.getRoom());
        }
        
        @Test
        @DisplayName("Constructor with edge times (0 and 23)")
        void testConstructorEdgeTimes() {
            Meeting earlyMeeting = new Meeting(0, 1, "Early");
            Meeting lateMeeting = new Meeting(22, 23, "Late");
            
            assertEquals(0, earlyMeeting.getStartTime());
            assertEquals(23, lateMeeting.getEndTime());
        }
        
        @Test
        @DisplayName("BUG-1: Constructor should reject invalid time range")
        void testBug1_InvalidTimeRange() {
            // BUG: startTime > endTime should throw exception but doesn't
            Meeting invalid = new Meeting(15, 10, "Invalid Meeting");
            
            // This test documents the bug - startTime is greater than endTime
            assertTrue(invalid.getStartTime() > invalid.getEndTime(),
                "BUG-1 DETECTED: Constructor accepts startTime > endTime (15 > 10)");
        }
        
        @Test
        @DisplayName("BUG-1: Constructor should reject same start/end time")
        void testBug1_SameStartEndTime() {
            // Zero-duration meeting should probably be invalid
            Meeting zeroDuration = new Meeting(10, 10, "Zero Duration");
            
            assertEquals(zeroDuration.getStartTime(), zeroDuration.getEndTime(),
                "BUG-1 VARIANT: Zero-duration meeting allowed");
        }
    }
    
    // ============ OVERLAP TESTS ============
    
    @Nested
    @DisplayName("Overlap Tests")
    class OverlapTests {
        
        @Test
        @DisplayName("Non-overlapping sequential meetings")
        void testNoOverlap_Sequential() {
            // 9-10 and 10-11 should NOT overlap
            assertFalse(meeting1.overlaps(meeting2),
                "Sequential meetings 9-10 and 10-11 should not overlap");
        }
        
        @Test
        @DisplayName("Overlapping meetings - partial overlap")
        void testOverlap_Partial() {
            Meeting overlapping = new Meeting(9, 11, "Long Meeting");
            // 9-10 and 9-11 should overlap
            assertTrue(meeting1.overlaps(overlapping));
        }
        
        @Test
        @DisplayName("Overlapping meetings - complete overlap")
        void testOverlap_Complete() {
            Meeting inner = new Meeting(9, 10, "Same Time");
            assertTrue(meeting1.overlaps(inner));
        }
        
        @Test
        @DisplayName("Overlapping meetings - one contains other")
        void testOverlap_Contains() {
            Meeting outer = new Meeting(8, 12, "All Day");
            assertTrue(meeting1.overlaps(outer));
            assertTrue(outer.overlaps(meeting1));
        }
        
        @Test
        @DisplayName("Non-overlapping meetings - gap between")
        void testNoOverlap_Gap() {
            Meeting later = new Meeting(14, 15, "Afternoon");
            assertFalse(meeting1.overlaps(later));
            assertFalse(later.overlaps(meeting1));
        }
        
        @Test
        @DisplayName("BUG-2: Adjacent meetings boundary check")
        void testBug2_AdjacentMeetings() {
            Meeting first = new Meeting(9, 10, "First");
            Meeting second = new Meeting(10, 11, "Second");
            
            // Adjacent meetings (end == start) should NOT overlap
            assertFalse(first.overlaps(second),
                "BUG-2: Adjacent meetings (9-10 and 10-11) incorrectly detected as overlapping");
            assertFalse(second.overlaps(first),
                "BUG-2: Reverse check also should not overlap");
        }
        
        @Test
        @DisplayName("Overlap symmetry check")
        void testOverlap_Symmetry() {
            Meeting a = new Meeting(9, 11, "A");
            Meeting b = new Meeting(10, 12, "B");
            
            // If A overlaps B, then B should overlap A
            assertEquals(a.overlaps(b), b.overlaps(a),
                "Overlap should be symmetric");
        }
    }
    
    // ============ GETTER/SETTER TESTS ============
    
    @Nested
    @DisplayName("Getter/Setter Tests")
    class GetterSetterTests {
        
        @Test
        @DisplayName("setStartTime updates value")
        void testSetStartTime() {
            meeting1.setStartTime(8);
            assertEquals(8, meeting1.getStartTime());
        }
        
        @Test
        @DisplayName("setEndTime updates value")
        void testSetEndTime() {
            meeting1.setEndTime(12);
            assertEquals(12, meeting1.getEndTime());
        }
        
        @Test
        @DisplayName("setDescription updates value")
        void testSetDescription() {
            meeting1.setDescription("Updated Meeting");
            assertEquals("Updated Meeting", meeting1.getDescription());
        }
        
        @Test
        @DisplayName("setRoom and getRoom work correctly")
        void testSetGetRoom() {
            Room room = new Room("Conference A");
            meeting1.setRoom(room);
            assertEquals(room, meeting1.getRoom());
        }
        
        @Test
        @DisplayName("Empty description is allowed")
        void testEmptyDescription() {
            Meeting meeting = new Meeting(9, 10, "");
            assertEquals("", meeting.getDescription());
        }
        
        @Test
        @DisplayName("Null description is allowed")
        void testNullDescription() {
            Meeting meeting = new Meeting(9, 10, null);
            assertNull(meeting.getDescription());
        }
    }
    
    // ============ TOSTRING TEST ============
    
    @Test
    @DisplayName("toString returns formatted string")
    void testToString() {
        String str = meeting1.toString();
        assertTrue(str.contains("9"));
        assertTrue(str.contains("10"));
        assertTrue(str.contains("Daily Standup"));
    }
}
