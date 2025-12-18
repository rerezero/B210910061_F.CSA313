# Lab 05: System Testing - Airport Connection

## Зорилго
Choice-based testing methodology ашиглан system-level тест хийх.

## Функцийн тодорхойлолт
`validConnection(flightA, flightB)` функц нь хоёр нислэгийн холболт хүчинтэй эсэхийг шалгана.

### Шаардлагууд
1. FlightA-н буух газар FlightB-н хөөрөх газартай ижил байх
2. Холболтын хугацаа 30 минут - 4 цаг байх
3. Олон улсаас дотоод руу шилжихэд 2+ цаг хэрэгтэй

## Choices

| Parameter | Choices |
|-----------|---------|
| Airport Match | Same, Different |
| Connection Time | TooShort (<30m), Valid (30m-4h), TooLong (>4h), Negative |
| Flight Types | Dom-Dom, Dom-Int, Int-Dom, Int-Int |

## Ажиллуулах
```bash
python test_airport_connection.py
```

## Test Cases

| TC | Airport | Time | Types | Expected |
|----|---------|------|-------|----------|
| TC01 | Same | Valid (60m) | Dom-Dom | Valid |
| TC02 | Different | Valid (60m) | Dom-Dom | Invalid |
| TC04 | Same | TooShort (15m) | Dom-Dom | Invalid |
| TC05 | Same | Valid (30m) | Dom-Dom | Valid |
| TC06 | Same | Valid (4h) | Dom-Dom | Valid |
| TC07 | Same | TooLong (5h) | Dom-Dom | Invalid |
| TC11 | Same | Valid (60m) | Int-Dom | Invalid |
| TC12 | Same | Valid (120m) | Int-Dom | Valid |

## Үр дүн
Бүх 12 тест амжилттай давсан.
