import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#chrome driver service


#Chrome
#service_obj = Service("C:\\Users\\USER\\OneDrive\\Documents\\Selenium Python_Udemy\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
#driver = webdriver.Chrome(service = service_obj) #line8, 9 this is used when you have vpn, oldversion

#FireFox
#service_obj = Service("gecko.exe") eg
#driver = webdriver.Chrome(service = service_obj)

#Edge
#service_obj = Service("msedgedriver.exe") eg
#driver = webdriver.Chrome(service = service_obj)


driver = webdriver.Edge()
driver.get("https://www.rahulshettyacademy.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)






time.sleep(2)