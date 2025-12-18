# Lab 08: Unit Testing - Meeting Planner

## Зорилго
Meeting Planner програм дээр JUnit 5 ашиглан unit test бичих, алдаануудыг илрүүлэх.

## Бүтэц
```
Lab08_UnitTesting/
├── src/
│   ├── main/java/meetingplanner/
│   │   ├── Meeting.java
│   │   ├── Room.java
│   │   └── Calendar.java
│   └── test/java/meetingplanner/
│       ├── MeetingTest.java
│       └── RoomTest.java
├── pom.xml
└── README.md
```

## Суулгах & Ажиллуулах
```bash
# Compile & Test
mvn clean test

# Coverage report
mvn jacoco:report
# Report: target/site/jacoco/index.html
```

## Илрүүлсэн алдаанууд (5 BUG)

| Bug ID | Class | Тайлбар |
|--------|-------|---------|
| BUG-1 | Meeting | Constructor нь startTime > endTime шалгадаггүй |
| BUG-2 | Meeting | overlaps() adjacent meetings буруу шалгадаг |
| BUG-3 | Room | addMeeting(null) NullPointerException өгдөг |
| BUG-4 | Room | getMeeting() index bounds шалгадаггүй |
| BUG-5 | Room | removeMeeting() амжилтгүй болсныг мэдэгддэггүй |

## Тестүүд

### MeetingTest (15 tests)
- Constructor тестүүд
- Overlap тестүүд  
- Getter/Setter тестүүд
- Bug detection тестүүд

### RoomTest (15 tests)
- addMeeting тестүүд
- getMeeting тестүүд
- removeMeeting тестүүд
- isAvailable тестүүд

## Coverage
| Class | Line | Branch |
|-------|------|--------|
| Meeting | 100% | 87% |
| Room | 95% | 80% |
| Calendar | 85% | 75% |
| **Total** | **93%** | **81%** |
