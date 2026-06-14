from selenium.webdriver.common.by import By

from pageObjects.checkout_comfirmation import Checkout_Confirmation
from utils.browserutils import BrowserUtils


class ShopPage(BrowserUtils):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.shop_link = (By.CSS_SELECTOR, "a[href*='shop']")
        self.product_link = (By.XPATH, "//div[@class='card h-100']")
        self.go_shop = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def add_to_cart(self, product_name):
        self.driver.find_element(*self.shop_link).click()
        products = self.driver.find_elements(*self.product_link)

        for i in products:
            productName = i.find_element(By.XPATH, "div/h4/a").text
            if productName == product_name:
                i.find_element(By.XPATH, "div/button").click()

    def go_to_shop(self):
        self.driver.find_element(* self.go_shop).click()

        checkout_confirmation = Checkout_Confirmation(self.driver)
        return checkout_confirmation



