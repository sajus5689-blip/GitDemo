#pytest -n 2 -m smoke --browser_name firefox --html=reports/report.html

import json
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.ShopPage import ShopPage
from pageObjects.login import LoginPage

test_data_path = '../data/test_e2eTestingFramework.json'
with open(test_data_path) as f:
    test_data = json.load(f) #load method convert your json file into python object
    test_list = test_data["data"]

@pytest.mark.smoke
@pytest.mark.parametrize("test_list_data", test_list)
def test_e2e(browserInstance, test_list_data):
    driver = browserInstance




    loginPage = LoginPage(driver)
    print(loginPage.getTitle())
    shopinpage = loginPage.login(test_list_data["userEmail"], test_list_data["UserPassword"])


    shopinpage.add_to_cart(test_list_data["productName"])
    print(shopinpage.getTitle())
    checkout_confirmation = shopinpage.go_to_shop()
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address("ind")
    checkout_confirmation.Validate()






    time.sleep(5)




