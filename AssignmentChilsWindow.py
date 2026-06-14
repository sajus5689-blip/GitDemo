import time


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



service_obj = Service("C:\\Users\\USER\\OneDrive\\Documents\\Selenium Python_Udemy\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.implicitly_wait(10)

driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()
newWindow = driver.window_handles

driver.switch_to.window(newWindow[1])
mail = driver.find_element(By.LINK_TEXT, "mentor@rahulshettyacademy.com").text

driver.switch_to.window(newWindow[0])
driver.find_element(By.XPATH, "//input[@id='username']").send_keys(mail)
driver.find_element(By.XPATH, "//input[@type='password']").send_keys(mail)
driver.find_element(By.XPATH, "//label[@class='customradio'][2]").click()
wait = WebDriverWait(driver, 10)
okay_button = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "button[id='okayBtn']")))
okay_button.click()
driver.find_element(By.CSS_SELECTOR, "button[id='okayBtn']").click()



driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()
time.sleep(2)
