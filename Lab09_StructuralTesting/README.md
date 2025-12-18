# Lab 09: Structural Testing - Code Coverage

## Зорилго
JaCoCo ашиглан Statement болон Branch coverage хэмжих.

## Lab08 дээр coverage ажиллуулах

```bash
cd ../Lab08_UnitTesting
mvn clean test jacoco:report
```

Coverage report: `target/site/jacoco/index.html`

## Coverage төрлүүд

### Statement Coverage
- Бүх код мөр шалгагдсан эсэх
- Target: 90%+

### Branch Coverage  
- Бүх if/else салаа шалгагдсан эсэх
- Target: 80%+

## Branch Coverage жишээ

```java
// overlaps() method - 4 branches
public boolean overlaps(Meeting other) {
    if (this.endTime > other.startTime &&    // Branch 1 & 2
        this.startTime < other.endTime) {     // Branch 3 & 4
        return true;
    }
    return false;
}
```

100% branch coverage-д шаардлагатай тестүүд:
1. Both conditions true -> return true
2. First false, second true -> return false  
3. First true, second false -> return false
4. Both false -> return false

## Үр дүн

| Class | Instructions | Branches | Lines |
|-------|--------------|----------|-------|
| Meeting.java | 98% | 100% | 100% |
| Room.java | 92% | 85% | 95% |
| Calendar.java | 88% | 80% | 90% |
| **Total** | **93%** | **88%** | **95%** |
