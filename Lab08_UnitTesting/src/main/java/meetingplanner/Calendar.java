package meetingplanner;

import java.util.HashMap;
import java.util.Map;
import java.util.Collection;

/**
 * Calendar class - Уулзалтын хуанли (өрөөнүүдийг удирдах)
 */
public class Calendar {
    private Map<String, Room> rooms;
    
    public Calendar() {
        this.rooms = new HashMap<>();
    }
    
    /**
     * Өрөө нэмэх
     * @param room Нэмэх өрөө
     */
    public void addRoom(Room room) {
        if (room == null) {
            throw new IllegalArgumentException("Room cannot be null");
        }
        rooms.put(room.getName(), room);
    }
    
    /**
     * Өрөө авах
     * @param name Өрөөний нэр
     * @return Room объект эсвэл null
     */
    public Room getRoom(String name) {
        return rooms.get(name);
    }
    
    /**
     * Өрөө устгах
     * @param name Өрөөний нэр
     * @return Устгагдсан өрөө эсвэл null
     */
    public Room removeRoom(String name) {
        return rooms.remove(name);
    }
    
    /**
     * Уулзалт товлох
     * @param roomName Өрөөний нэр
     * @param meeting Уулзалт
     * @return true хэрэв амжилттай товлогдвол
     */
    public boolean scheduleMeeting(String roomName, Meeting meeting) {
        Room room = rooms.get(roomName);
        if (room == null) {
            return false;
        }
        return room.addMeeting(meeting);
    }
    
    /**
     * Бүх өрөөнөөс завтай өрөө хайх
     * @param startTime Эхлэх цаг
     * @param endTime Дуусах цаг
     * @return Завтай өрөөний нэр эсвэл null
     */
    public String findAvailableRoom(int startTime, int endTime) {
        for (Room room : rooms.values()) {
            if (room.isAvailable(startTime, endTime)) {
                return room.getName();
            }
        }
        return null;
    }
    
    /**
     * Бүх өрөөнүүдийг авах
     * @return Өрөөнүүдийн цуглуулга
     */
    public Collection<Room> getAllRooms() {
        return rooms.values();
    }
    
    /**
     * Өрөөний тоо
     * @return Өрөөний тоо
     */
    public int getRoomCount() {
        return rooms.size();
    }
}
