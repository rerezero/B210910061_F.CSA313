# Лаборатори 07: Exploratory Testing Session Report

## Session Information
- **Application:** Gerege Mobile App
- **Tester:** Munkhzorig
- **Date:** 2024-11-15
- **Duration:** 60 minutes
- **Charter:** Төлбөр хийх үйлдлүүдийг шалгах
- **Environment:** Android 13, Samsung Galaxy S21

---

## Session Timeline

### 00:00 - 10:00: Апп суулгах, бүртгүүлэх
- ✅ Play Store-оос татах амжилттай
- ✅ Бүртгэлийн форм сайн ажиллаж байна
- ✅ OTP код 2 минутын дараа дуусгавар болно
- ✅ Утасны дугаар баталгаажуулалт ажиллаж байна

### 10:00 - 25:00: Данс нэмэх функц
- ✅ Банкны жагсаалт бүрэн харагдаж байна
- ❌ **BUG-001:** Банкны карт нэмэхэд "Network Error" гарч байна
- ❌ **BUG-002:** Карт нэмсний дараа буцах товч ажиллахгүй
- ✅ Хадгаламжийн данс нэмэх ажиллаж байна

### 25:00 - 40:00: Төлбөр хийх
- ✅ QR уншуулах хурдан ажиллаж байна
- ✅ Гар утасны дугаараар шилжүүлэг ажиллаж байна
- ❌ **BUG-003:** 0 төгрөг шилжүүлэх оролдлогод validation байхгүй
- ❌ **BUG-004:** Сөрөг тоо оруулахад апп crash болж байна
- ❌ **BUG-005:** 10 оронтой тоо оруулахад UI алдаа гарч байна

### 40:00 - 55:00: Түүх, тайлан
- ✅ Гүйлгээний түүх зөв харагдаж байна
- ✅ Огноогоор шүүх ажиллаж байна
- ❌ **BUG-006:** PDF татах үед апп удаан ачаалагдаж байна (15+ сек)
- ✅ Тайлан export ажиллаж байна

### 55:00 - 60:00: Тохиргоо
- ✅ Хэл солих функц ажиллаж байна
- ✅ Dark mode сайн харагдаж байна
- ✅ Notification тохиргоо ажиллаж байна

---

## Bug Reports

### BUG-001: Карт нэмэхэд Network Error
| Field | Value |
|-------|-------|
| **ID** | BUG-001 |
| **Summary** | Банкны карт нэмэхэд "Network Error" гарч байна |
| **Severity** | High |
| **Priority** | High |
| **Steps** | 1. Апп нээх → 2. Данс нэмэх → 3. Карт нэмэх → 4. Картын мэдээлэл оруулах |
| **Expected** | Карт амжилттай нэмэгдэх |
| **Actual** | "Network Error" алдаа гарч байна (WiFi-д холбогдсон байсан ч) |

### BUG-002: Буцах товч ажиллахгүй
| Field | Value |
|-------|-------|
| **ID** | BUG-002 |
| **Summary** | Карт нэмсний дараа буцах товч ажиллахгүй |
| **Severity** | Medium |
| **Priority** | Medium |
| **Steps** | 1. Карт нэмэх оролдлого → 2. Алдаа гарах → 3. Буцах товч дарах |
| **Expected** | Өмнөх хуудас руу буцах |
| **Actual** | Юу ч болохгүй, товч react хийхгүй |

### BUG-003: 0 төгрөг validation байхгүй
| Field | Value |
|-------|-------|
| **ID** | BUG-003 |
| **Summary** | 0 төгрөг шилжүүлэх оролдлогод validation байхгүй |
| **Severity** | Low |
| **Priority** | Low |
| **Steps** | 1. Мөнгө шилжүүлэх → 2. Дүн: 0 оруулах → 3. Илгээх дарах |
| **Expected** | "Дүн 0-ээс их байх ёстой" алдаа |
| **Actual** | Хүсэлт илгээгдэж байна |

### BUG-004: Сөрөг тоонд crash (CRITICAL)
| Field | Value |
|-------|-------|
| **ID** | BUG-004 |
| **Summary** | Сөрөг тоо оруулахад апп crash болж байна |
| **Severity** | Critical |
| **Priority** | High |
| **Steps** | 1. Мөнгө шилжүүлэх → 2. Дүн: -1000 оруулах → 3. Илгээх дарах |
| **Expected** | Validation алдаа харуулах |
| **Actual** | Апп crash болж хаагдана |
| **Attachment** | crash_log.txt |

### BUG-005: UI алдаа том тоонд
| Field | Value |
|-------|-------|
| **ID** | BUG-005 |
| **Summary** | 10 оронтой тоо оруулахад UI алдаа |
| **Severity** | Low |
| **Priority** | Medium |
| **Steps** | 1. Дүн талбарт 9999999999 оруулах |
| **Expected** | Тоо зөв харагдах эсвэл хязгаарлах |
| **Actual** | Тоо UI-аас гадагш гарч харагдахгүй |

### BUG-006: PDF татах удаан
| Field | Value |
|-------|-------|
| **ID** | BUG-006 |
| **Summary** | PDF татах үед апп удаан ачаалагдаж байна |
| **Severity** | Low |
| **Priority** | Medium |
| **Steps** | 1. Түүх → 2. Тайлан → 3. PDF татах |
| **Expected** | 3-5 секундэд татагдах |
| **Actual** | 15+ секунд, loading indicator байхгүй |

---

## Session Metrics

| Metric | Value |
|--------|-------|
| Total Time | 60 minutes |
| Bugs Found | 6 |
| Critical | 1 |
| High | 1 |
| Medium | 2 |
| Low | 2 |
| Test Coverage | ~70% of Payment module |
| Areas Not Tested | International transfers, Scheduled payments |

---

## Recommendations

1. **BUG-004 яаралтай засах** - Апп crash нь хэрэглэгчийн туршлагад маш муугаар нөлөөлнө
2. Input validation бүх талбарт нэмэх
3. Network error handling сайжруулах
4. Loading indicator нэмэх
5. Буцах товчны navigation засах

---

## Session Notes

- Апп ерөнхийдөө сайн ажиллаж байна
- UI/UX сайн боловсруулагдсан
- Гол асуудал: Input validation дутмаг
- Performance: QR scan хурдан, PDF татах удаан
