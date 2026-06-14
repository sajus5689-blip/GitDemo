from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

BrowserSortedList=[]

service_obj = Service("C:\\Users\\USER\\OneDrive\\Documents\\Selenium Python_Udemy\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.implicitly_wait(10)

#click on the column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()


#collect all veggies name -> BrowserSortedList
veggiesWebElement = driver.find_elements(By.XPATH, "//tr/td[1]")
for i in veggiesWebElement:
    BrowserSortedList.append(i.text)

OriginalSortedList = BrowserSortedList.copy()

#Sort BrowserSortedList
BrowserSortedList.sort()

assert BrowserSortedList == OriginalSortedList