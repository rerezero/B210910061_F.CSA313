package meetingplanner;

/**
 * Meeting class - Уулзалтын мэдээлэл хадгалах
 * 
 * BUGS FOUND:
 * - BUG-1: Constructor does not validate startTime > endTime
 * - BUG-2: overlaps() uses > instead of >= for boundary check
 */
public class Meeting {
    private int startTime;  // 0-23 format (hours)
    private int endTime;
    private String description;
    private Room room;
    
    /**
     * Meeting үүсгэх
     * @param startTime Эхлэх цаг (0-23)
     * @param endTime Дуусах цаг (0-23)
     * @param description Тайлбар
     * 
     * BUG-1: startTime > endTime үед алдаа өгөх ёстой боловч өгөхгүй байна
     */
    public Meeting(int startTime, int endTime, String description) {
        // BUG-1: No validation for startTime > endTime
        // Should throw IllegalArgumentException if startTime >= endTime
        this.startTime = startTime;
        this.endTime = endTime;
        this.description = description;
    }
    
    /**
     * Хоёр уулзалт давхцаж байгаа эсэхийг шалгах
     * @param other Харьцуулах уулзалт
     * @return true хэрэв давхцаж байвал
     * 
     * BUG-2: Adjacent meetings (9-10 and 10-11) should NOT overlap
     * Current: endTime > other.startTime (returns true for 10 > 10 = false, OK)
     * But: startTime < other.endTime could cause issues with >= comparison
     */
    public boolean overlaps(Meeting other) {
        // BUG-2: Logic issue - boundary cases not handled correctly
        // Adjacent meetings (end == other.start) should NOT overlap
        if (this.endTime > other.startTime && this.startTime < other.endTime) {
            return true;
        }
        return false;
    }
    
    // Getters and Setters
    public int getStartTime() {
        return startTime;
    }
    
    public void setStartTime(int startTime) {
        this.startTime = startTime;
    }
    
    public int getEndTime() {
        return endTime;
    }
    
    public void setEndTime(int endTime) {
        this.endTime = endTime;
    }
    
    public String getDescription() {
        return description;
    }
    
    public void setDescription(String description) {
        this.description = description;
    }
    
    public Room getRoom() {
        return room;
    }
    
    public void setRoom(Room room) {
        this.room = room;
    }
    
    @Override
    public String toString() {
        return String.format("Meeting[%d:00-%d:00, %s]", startTime, endTime, description);
    }
}
