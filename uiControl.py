import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\Users\\USER\\OneDrive\\Documents\\Selenium Python_Udemy\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes))

for i in checkboxes:
    if i.get_attribute("value") == "option2":
        i.click()
        time.sleep(5)
        assert i.is_selected() == True
        break

radiobutton = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
print(len(radiobutton))
radiobutton[2].click()
time.sleep(5)
assert radiobutton[2].is_selected()

assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()
time.sleep(5)