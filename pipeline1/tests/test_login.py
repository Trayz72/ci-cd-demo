from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

print("Starting Selenium Demo")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("http://127.0.0.1:5050")
time.sleep(2)

driver.find_element(By.NAME, "username").send_keys("admin")
time.sleep(1)
driver.find_element(By.NAME, "password").send_keys("secret")
time.sleep(1)
driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
time.sleep(3)

if "Login successful!" in driver.page_source:
    print("Test Passed!")
else:
    print("Test Failed")

driver.quit()
print("Demo Complete!")