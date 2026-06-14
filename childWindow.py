from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\Users\\USER\\OneDrive\\Documents\\Selenium Python_Udemy\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)

driver.get("https://the-internet.herokuapp.com/windows")
driver.implicitly_wait(10)

driver.find_element(By.LINK_TEXT, "Click Here").click()
WindowOpen = driver.window_handles

driver.switch_to.window(WindowOpen[1])
print(driver.find_element(By.TAG_NAME, "h3").text)

driver.switch_to.window(WindowOpen[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text


