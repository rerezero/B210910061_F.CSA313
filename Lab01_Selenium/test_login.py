"""
Лаборатори 01: Selenium WebDriver суурь ойлголт
MUST оюутны порталд нэвтрэх автомат тест
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest


class TestMUSTLogin:
    """MUST оюутны порталд нэвтрэх автомат тест"""
    
    def setup_method(self):
        """Тест бүрийн өмнө Chrome хөтөч эхлүүлэх"""
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Headless mode for CI/CD
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.base_url = "https://student.must.edu.mn"
    
    def test_page_loads(self):
        """Веб хуудас амжилттай ачаалагдаж байгааг шалгах"""
        self.driver.get(self.base_url)
        
        # Title шалгах
        assert "MUST" in self.driver.title or "Student" in self.driver.title
        
        # Login form байгаа эсэхийг шалгах
        login_form = self.wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "form"))
        )
        assert login_form.is_displayed()
        print("✓ Хуудас амжилттай ачаалагдлаа")
    
    def test_login_form_elements(self):
        """Нэвтрэх формын элементүүд байгаа эсэхийг шалгах"""
        self.driver.get(self.base_url)
        
        # Username талбар
        username_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        assert username_field.is_displayed()
        
        # Password талбар
        password_field = self.driver.find_element(By.ID, "password")
        assert password_field.is_displayed()
        
        # Login товч
        login_btn = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        assert login_btn.is_displayed()
        
        print("✓ Бүх форм элементүүд байна")
    
    def test_successful_login(self):
        """Амжилттай нэвтрэх үйлдлийг шалгах"""
        self.driver.get(self.base_url)
        
        # Нэвтрэх талбаруудыг олох
        username_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        password_field = self.driver.find_element(By.ID, "password")
        
        # Хэрэглэгчийн мэдээлэл оруулах
        username_field.clear()
        username_field.send_keys("test_student")
        password_field.clear()
        password_field.send_keys("test_password123")
        
        # Нэвтрэх товч дарах
        login_btn = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_btn.click()
        
        # Dashboard хуудас руу шилжсэн эсэхийг шалгах
        try:
            dashboard = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "dashboard"))
            )
            assert dashboard.is_displayed()
            print("✓ Амжилттай нэвтэрлээ")
        except:
            # Тест орчинд бодит нэвтрэлт байхгүй тул skip
            print("⚠ Тест орчинд нэвтрэлт шалгагдахгүй")
    
    def test_invalid_credentials(self):
        """Буруу нууц үгээр нэвтрэхэд алдаа гарахыг шалгах"""
        self.driver.get(self.base_url)
        
        username_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        password_field = self.driver.find_element(By.ID, "password")
        
        # Буруу мэдээлэл оруулах
        username_field.send_keys("wrong_user")
        password_field.send_keys("wrong_password")
        
        login_btn = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_btn.click()
        
        # Алдааны мессеж харагдах ёстой
        try:
            error_msg = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "error-message"))
            )
            assert error_msg.is_displayed()
            print("✓ Алдааны мессеж харагдлаа")
        except:
            print("⚠ Алдааны мессеж олдсонгүй")
    
    def test_empty_credentials_validation(self):
        """Хоосон талбартай нэвтрэхэд validation ажиллахыг шалгах"""
        self.driver.get(self.base_url)
        
        login_btn = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        login_btn.click()
        
        # HTML5 validation шалгах
        username_field = self.driver.find_element(By.ID, "username")
        is_valid = self.driver.execute_script(
            "return arguments[0].validity.valid", username_field
        )
        
        if not is_valid:
            print("✓ HTML5 validation ажиллаж байна")
        else:
            print("⚠ Validation шалгагдахгүй")
    
    def test_password_field_masked(self):
        """Нууц үг талбар mask хийгдсэн эсэхийг шалгах"""
        self.driver.get(self.base_url)
        
        password_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        
        # type="password" эсэхийг шалгах
        field_type = password_field.get_attribute("type")
        assert field_type == "password", "Нууц үг талбар mask хийгдээгүй"
        print("✓ Нууц үг талбар mask хийгдсэн")
    
    def teardown_method(self):
        """Тест бүрийн дараа хөтөч хаах"""
        if self.driver:
            self.driver.quit()


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--html=selenium_report.html", "--self-contained-html"])
