import time
import tempfile
import shutil
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
@pytest.fixture(scope="module")
def driver():
    temp_profile = tempfile.mkdtemp()
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument(f"--user-data-dir={temp_profile}")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
    shutil.rmtree(temp_profile)
def test_valid_login(driver):
    driver.get("http://flask-service:80")
    time.sleep(1)
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("admin123")
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    assert "Welcome, admin" in driver.page_source
