import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service("C:\\Users\\USER\\OneDrive\\Documents\\Selenium Python_Udemy\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries))

for i in countries:
    if i.text == "India":
        i.click()
        break

#print(driver.find_element(By.ID, "autosuggest").text) -> This method wont work because the dropdown is dynamically selected

#print(driver.find_element(By.ID, "autosuggest").get_attribute("value")) -> This will work for dynamic dropdown
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "BASIndia"





