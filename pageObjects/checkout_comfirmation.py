from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.browserutils import BrowserUtils


class Checkout_Confirmation(BrowserUtils):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.checkout_button = (By.XPATH, "//button[@class='btn btn-success']")
        self.country_name = (By.XPATH, "//input[@id='country']")
        self.country = (By.LINK_TEXT, "India")
        self.checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
        self.submit = (By.CSS_SELECTOR, "input[type='submit']")
        self.validation = (By.CLASS_NAME, "alert-success")



    def checkout(self):
        self.driver.find_element(*self.checkout_button).click()

    def enter_delivery_address(self, countryName):
        self.driver.find_element(*self.country_name).send_keys(countryName)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((self.country)))
        self.driver.find_element(*self.country).click()
        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.submit).click()

    def Validate(self):
        Message = self.driver.find_element(*self.validation).text

        assert "Success! Thank you!" in Message


