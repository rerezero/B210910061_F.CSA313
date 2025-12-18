# Lab 03: Postman ашиглан API туршилт

## Зорилго
Postman болон Newman ашиглан Binance API-н функционал тест хийх.

## Суулгах
```bash
npm install -g newman newman-reporter-htmlextra
```

## Ажиллуулах

### Postman дээр
1. Postman нээх
2. Import -> binance-collection.json
3. Run collection

### Newman CLI
```bash
# Энгийн ажиллуулах
newman run binance-collection.json

# 100 удаа давтах
newman run binance-collection.json -n 100

# HTML тайлан үүсгэх
newman run binance-collection.json -r htmlextra --reporter-htmlextra-export report.html
```

## Тестүүд
1. **Get BTC Price** - BTC үнэ авах (5 тест)
2. **Get ETH Price** - ETH үнэ авах (3 тест)
3. **Get All Prices** - Бүх үнэ авах (4 тест)
4. **Invalid Symbol** - Алдааны тест (3 тест)
5. **Get 24hr Ticker** - 24 цагийн мэдээлэл (2 тест)

## Үр дүн
- Нийт: 17 тест
- Passed: 17
- Failed: 0
