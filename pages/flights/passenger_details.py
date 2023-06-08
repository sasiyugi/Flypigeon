from selenium.webdriver.common.by import By

from Base.base_class import base_class
from utilities.utils import Utils
import logging
class passenger_details(base_class):

    log = Utils.custom_logger()
    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver

    #Locators
    proceed_locator = "//button[normalize-space()='Proceed']"
    customer_mobile_number_locator = "mobile"
    customer_email_locator = "email"
    title_locator = "gender"

    def proceed_locators(self):
        return self.webelement_click(By.XPATH, self.proceed_locator)

    def customer_mobile_locators(self):
        return self.webelement_click(By.ID, self.customer_mobile_number_locator)

    def customer_email_locators(self):
        return self.webelement_click(By.ID, self.customer_email_locator)

    def title_locators(self):
        return self.drop_down(By.ID, self.title_locator)

    def proceed_button_click(self):
        self.proceed_locators().click()
        self.log.info("Proceed button clicked")

    def customer_mobile(self, mobile_data):
        self.customer_mobile_locators().send_keys(mobile_data)
        self.log.info("Mobile number is placed")

    def customer_email(self, email_data):
        self.customer_email_locators().click()
        self.customer_email_locators().send_keys(email_data)
        self.log.info("email is placed")

    def customer_title(self, customer_type):
        self.title_locators().select_by_value(customer_type)
        self.log.info("Customer_tilte is placed")

    def passenger_details(self, mobile_data, email_data, customer_type):
        self.customer_mobile(mobile_data)
        self.customer_email(email_data)
        self.customer_title(customer_type)
