import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

service_obj = Service()
driver = webdriver.Chrome(service = service_obj)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for i in products:
    productName = i.find_element(By.XPATH, "div/h4/a").text
    if productName == "Blackberry":
        i.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
driver.find_element(By.XPATH, "//input[@id='country']").send_keys("ind")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
Message = driver.find_element(By.CLASS_NAME, "alert-success").text

assert "Success! Thank you!" in Message



