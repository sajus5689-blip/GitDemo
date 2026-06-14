import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

service_obj = Service("C:\\Users\\USER\\OneDrive\\Documents\\Selenium Python_Udemy\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.implicitly_wait(5)

actions = ActionChains(driver)

actions.move_to_element(driver.find_element(By.ID, "mousehover")).perform()

actions.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()

actions.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()

#actions.double_click(By.)
#actions.drag_and_drop()


