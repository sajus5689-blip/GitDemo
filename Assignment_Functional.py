import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

ExpectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actualList = []

service_obj = Service("C:\\Users\\USER\\OneDrive\\Documents\\Selenium Python_Udemy\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)

driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(5)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")

count = len(results)
assert count > 0

for i in results:
    actualList.append(i.find_element(By.XPATH, "h4").text)
    i.find_element(By.XPATH, "div/button").click()
assert ExpectedList == actualList

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()

driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")

driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(driver, 10)  # Explicit Wait
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))
promotion = driver.find_element(By.CLASS_NAME, "promoInfo").text
print(promotion)
assert "Code" in promotion

#Sum validation

prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for i in prices:
    sum = sum + int(i.text)
print(sum)
totalprice = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert sum == totalprice

discountedAmount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
assert totalprice > discountedAmount