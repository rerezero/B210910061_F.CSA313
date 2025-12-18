package meetingplanner;

import java.util.ArrayList;
import java.util.List;

/**
 * Room class - Уулзалтын өрөө
 * 
 * BUGS FOUND:
 * - BUG-3: addMeeting() does not check for null input
 * - BUG-4: getMeeting() does not validate index bounds
 * - BUG-5: removeMeeting() does not indicate if meeting was not found
 */
public class Room {
    private String name;
    private List<Meeting> meetings;
    
    public Room(String name) {
        this.name = name;
        this.meetings = new ArrayList<>();
    }
    
    /**
     * Өрөөнд уулзалт нэмэх
     * @param meeting Нэмэх уулзалт
     * @return true хэрэв амжилттай нэмэгдвэл
     * 
     * BUG-3: Null meeting passed will cause NullPointerException in loop
     */
    public boolean addMeeting(Meeting meeting) {
        // BUG-3: No null check - should throw IllegalArgumentException or return false
        // if (meeting == null) throw new IllegalArgumentException("Meeting cannot be null");
        
        for (Meeting existing : meetings) {
            if (existing.overlaps(meeting)) {
                return false;  // Cannot add overlapping meeting
            }
        }
        
        meeting.setRoom(this);
        meetings.add(meeting);
        return true;
    }
    
    /**
     * Index-ээр уулзалт авах
     * @param index Уулзалтын индекс
     * @return Meeting объект
     * 
     * BUG-4: No bounds checking - will throw IndexOutOfBoundsException
     */
    public Meeting getMeeting(int index) {
        // BUG-4: No index validation
        // Should check: if (index < 0 || index >= meetings.size()) 
        //               throw new IndexOutOfBoundsException("Invalid index: " + index);
        return meetings.get(index);
    }
    
    /**
     * Уулзалт устгах
     * @param meeting Устгах уулзалт
     * 
     * BUG-5: Does not return boolean or throw exception if meeting not found
     */
    public void removeMeeting(Meeting meeting) {
        // BUG-5: Should return boolean indicating success/failure
        // boolean removed = meetings.remove(meeting);
        // if (!removed) throw new IllegalArgumentException("Meeting not found");
        meetings.remove(meeting);
    }
    
    /**
     * Бүх уулзалтыг цэвэрлэх
     */
    public void clearMeetings() {
        for (Meeting m : meetings) {
            m.setRoom(null);
        }
        meetings.clear();
    }
    
    /**
     * Тодорхой цагт өрөө завтай эсэхийг шалгах
     * @param startTime Эхлэх цаг
     * @param endTime Дуусах цаг
     * @return true хэрэв завтай бол
     */
    public boolean isAvailable(int startTime, int endTime) {
        Meeting temp = new Meeting(startTime, endTime, "temp");
        for (Meeting existing : meetings) {
            if (existing.overlaps(temp)) {
                return false;
            }
        }
        return true;
    }
    
    // Getters
    public String getName() {
        return name;
    }
    
    public List<Meeting> getMeetings() {
        return new ArrayList<>(meetings);  // Return copy to prevent modification
    }
    
    public int getMeetingCount() {
        return meetings.size();
    }
    
    @Override
    public String toString() {
        return String.format("Room[%s, meetings=%d]", name, meetings.size());
    }
}
