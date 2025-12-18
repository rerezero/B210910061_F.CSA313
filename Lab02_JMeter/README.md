# Lab 02: JMeter ашиглан гүйцэтгэлийн туршилт

## Зорилго
Apache JMeter ашиглан Binance API-н гүйцэтгэлийн туршилт хийх.

## Тохиргоо
- Thread Group: 100 хэрэглэгч
- Ramp-Up: 10 секунд
- Loop Count: 5

## Ажиллуулах

### GUI горимоор
```bash
jmeter -t binance_test.jmx
```

### Non-GUI горимоор
```bash
jmeter -n -t binance_test.jmx -l results.jtl -e -o ./report
```

### HTML тайлан үүсгэх
```bash
jmeter -g results.jtl -o html_report/
```

## Endpoints
1. **Get BTC Price**: `/api/v3/ticker/price?symbol=BTCUSDT`
2. **Get All Prices**: `/api/v3/ticker/price`

## Үр дүн
| Metric | Value |
|--------|-------|
| Samples | 1000 |
| Average | 264ms |
| Throughput | 48.2/sec |
| Error % | 0.2% |
