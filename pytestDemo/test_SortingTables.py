from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def test_sort(browserInstance):
    driver = browserInstance
    BrowserSortedList = []


    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    driver.implicitly_wait(10)

    # click on the column header
    driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

    # collect all veggies name -> BrowserSortedList
    veggiesWebElement = driver.find_elements(By.XPATH, "//tr/td[1]")
    for i in veggiesWebElement:
        BrowserSortedList.append(i.text)

    OriginalSortedList = BrowserSortedList.copy()

    # Sort BrowserSortedList
    BrowserSortedList.sort()

    assert BrowserSortedList == OriginalSortedList