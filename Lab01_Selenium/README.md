# Lab 01: Selenium WebDriver суурь ойлголт

## Зорилго
Selenium WebDriver ашиглан MUST оюутны порталд нэвтрэх функцийг автоматаар туршилт хийх.

## Суулгах
```bash
pip install -r requirements.txt
```

## Ажиллуулах
```bash
# Бүх тест ажиллуулах
pytest test_login.py -v

# HTML тайлан үүсгэх
pytest test_login.py --html=report.html --self-contained-html
```

## Тестүүд
- `test_page_loads` - Хуудас ачаалагдаж байгааг шалгах
- `test_login_form_elements` - Форм элементүүд байгаа эсэх
- `test_successful_login` - Амжилттай нэвтрэх
- `test_invalid_credentials` - Буруу мэдээллээр нэвтрэх
- `test_empty_credentials_validation` - Хоосон талбар validation
- `test_password_field_masked` - Нууц үг mask хийгдсэн эсэх

## Үр дүн
Бүх 6 тест амжилттай давсан.
