from selenium.webdriver.common.by import By

from Base.base_class import base_class
from pages.flights.passenger_details import passenger_details
from utilities.utils import Utils


class showing_flights(base_class):
    log = Utils.custom_logger()
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    book_now_locator = "//button[contains(text(), 'Book Now')][1]"
    showingflight = "//h3[normalize-space()='Showing best flights']"

    def book_now_locators(self):
        return self.webelement_click(By.XPATH, self.book_now_locator)

    def showing_flights_data(self):
        return self.webelement_click(By.XPATH, self.showingflight)

    def booknow_button_click(self):
        self.book_now_locators().click()
        self.log.info("Book now button Clicked")
        pd = passenger_details(self.driver)
        return pd
