import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ChromeOptions = webdriver.ChromeOptions()
ChromeOptions.add_argument('--ignore-certificate-errors')
ChromeOptions.add_argument('headless')

service_obj = Service("C:\\Users\\USER\\OneDrive\\Documents\\Selenium Python_Udemy\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service = service_obj, options = ChromeOptions)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(10)

driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("screen.png")
time.sleep(5)