# Lab 04: Dynamic Mock Server

## Зорилго
Express.js ашиглан динамик Mock Server үүсгэх.

## Суулгах
```bash
npm install
```

## Ажиллуулах
```bash
npm start
# эсвэл
node server.js
```

## Endpoints

### Users
| Method | Endpoint | Тайлбар |
|--------|----------|---------|
| GET | /users | Бүх хэрэглэгчид |
| GET | /users/:id | Нэг хэрэглэгч |
| POST | /users | Шинэ хэрэглэгч |
| PUT | /users/:id | Хэрэглэгч засах |
| DELETE | /users/:id | Хэрэглэгч устгах |

### Transactions
| Method | Endpoint | Тайлбар |
|--------|----------|---------|
| POST | /transfer | Мөнгө шилжүүлэх |
| GET | /transactions | Гүйлгээний түүх |

### Admin
| Method | Endpoint | Тайлбар |
|--------|----------|---------|
| POST | /admin/reset | Сервер reset |
| POST | /admin/simulate-error | Алдаа симуляц |
| POST | /admin/simulate-delay | Delay симуляц |
| GET | /admin/stats | Статистик |

## Жишээ хүсэлтүүд
```bash
# Бүх хэрэглэгчид
curl http://localhost:3000/users

# Шинэ хэрэглэгч
curl -X POST http://localhost:3000/users \
  -H "Content-Type: application/json" \
  -d '{"name": "Дорж", "email": "dorj@test.com", "balance": 50000}'

# Мөнгө шилжүүлэх
curl -X POST http://localhost:3000/transfer \
  -H "Content-Type: application/json" \
  -d '{"fromId": 1, "toId": 2, "amount": 10000}'
```
