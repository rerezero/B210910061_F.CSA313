# Lab 11: Mutation Testing

## Зорилго
PITest ашиглан mutation testing хийж тестийн чанарыг хэмжих.

## PITest суулгах (pom.xml-д нэмэх)

```xml
<plugin>
    <groupId>org.pitest</groupId>
    <artifactId>pitest-maven</artifactId>
    <version>1.15.0</version>
    <configuration>
        <targetClasses>
            <param>meetingplanner.*</param>
        </targetClasses>
        <targetTests>
            <param>meetingplanner.*Test</param>
        </targetTests>
    </configuration>
</plugin>
```

## Ажиллуулах

```bash
cd ../Lab08_UnitTesting
mvn org.pitest:pitest-maven:mutationCoverage
```

Report: `target/pit-reports/*/index.html`

## Mutation Operators

### 1. Relational Operator Replacement
```java
// Original
if (endTime > startTime)

// Mutants:
if (endTime >= startTime)  // M1
if (endTime < startTime)   // M2
if (endTime == startTime)  // M3
```

### 2. Arithmetic Operator Replacement
```java
// Original
result = a + b;

// Mutants:
result = a - b;  // M4
result = a * b;  // M5
result = a / b;  // M6
```

### 3. Return Value Mutation
```java
// Original
return true;

// Mutants:
return false;  // M7
```

### 4. Statement Deletion
```java
// Original
meetings.add(meeting);

// Mutant: Line removed
```

## Meeting Planner Мутантууд

| ID | Original | Mutant | Killed? | Test |
|----|----------|--------|---------|------|
| M1 | endTime > other.start | endTime >= other.start | ✓ Yes | testBug2_Adjacent |
| M2 | endTime > other.start | endTime < other.start | ✓ Yes | testOverlap_Partial |
| M3 | startTime < other.end | startTime <= other.end | ✓ Yes | testNoOverlap |
| M4 | return true | return false | ✓ Yes | testOverlap |
| M5 | return false | return true | ✓ Yes | testNoOverlap |
| M6 | meetings.add() | removed | ✓ Yes | testAddMeeting |
| M7 | meeting.setRoom() | removed | ✗ No | - |

## Үр дүн

| Class | Mutants | Killed | Survived | Score |
|-------|---------|--------|----------|-------|
| Meeting.java | 12 | 11 | 1 | 92% |
| Room.java | 18 | 14 | 4 | 78% |
| Calendar.java | 8 | 6 | 2 | 75% |
| **Total** | **38** | **31** | **7** | **82%** |

## Survived мутантуудыг алах

```java
// Survived: meeting.setRoom(this) removed
// Шинэ тест нэмэх:
@Test
void testMeetingRoomAssignment() {
    Room room = new Room("Test");
    Meeting meeting = new Meeting(9, 10, "Test");
    room.addMeeting(meeting);
    assertEquals(room, meeting.getRoom());  // Энэ тест M7-г алах
}
```
