import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--ignore-ssl-errors")
    
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

def test_dashboard_accessibility(driver):
    domain = os.getenv('DOMAIN_NAME', 'siem.example.com')
    url = f"https://{domain}"
    
    driver.get(url)
    wait = WebDriverWait(driver, 30)
    
    # Check page loads and title contains Wazuh
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    assert "Wazuh" in driver.title

def test_login_form_present(driver):
    domain = os.getenv('DOMAIN_NAME', 'siem.example.com')
    url = f"https://{domain}"
    
    driver.get(url)
    wait = WebDriverWait(driver, 30)
    
    # Check login form elements exist
    username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    password_field = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.TYPE, "submit")
    
    assert username_field.is_displayed()
    assert password_field.is_displayed()
    assert login_button.is_displayed()
