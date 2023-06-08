import logging

from selenium.webdriver.common.by import By

from Base.base_class import base_class
from pages.flights.showing_filghts import showing_flights
from utilities.utils import Utils


class oneway(base_class):

    log = Utils.custom_logger()
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    oneway_from_locator = "(//input[@id='standard-basic'])[1]"
    oneway_from_table = "//ul[@class='AirportAutocompleteInput_airportAutocompleteList__10xsx']//li"
    oneway_to_locator = "(//input[@id='standard-basic'])[2]"
    oneway_to_table = "//ul[@class='AirportAutocompleteInput_airportAutocompleteList__10xsx']//descendant::li"
    calendar = "div[class='MuiOutlinedInput-root MuiInputBase-root MuiInputBase-colorPrimary MuiInputBase-formControl MuiInputBase-adornedEnd css-1bn53lx']"
    calendar_table = "//div[@class='PrivatePickersSlideTransition-root css-dhopo2']//descendant::div"
    search = "//button[text()='Search Flight']"

    def oneway_from_locators(self):
        return self.webelement_click(By.XPATH, self.oneway_from_locator)

    def oneway_from_tables(self):
        return self.find_webelements(By.XPATH, self.oneway_from_table)

    def one_way_to_locators(self):
        return self.webelement_click(By.XPATH, self.oneway_to_locator)

    def oneway_to_tables(self):
        return self.find_webelements(By.XPATH, self.oneway_to_table)

    def calendars(self):
        return self.webelement_click(By.CSS_SELECTOR, self.calendar)

    def calendar_tables(self):
        return self.find_webelements(By.XPATH, self.calendar_table)

    def search_button(self):
        return self.webelement_click(By.XPATH, self.search)

    def from_field(self, from_, from_data):
        self.log.warning("Enter From Location")
        self.oneway_from_locators().click()
        self.oneway_from_locators().send_keys(from_)

        leaving_from = self.oneway_from_tables()
        for leave in leaving_from:
            if from_data in leave.text:
                leave.click()
                break

        self.log.info("From location is placed")

    def to_field(self, to_, to_data):
        self.log.warning("Enter To Location")
        self.one_way_to_locators().click()
        self.one_way_to_locators().send_keys(to_)

        going_to = self.oneway_to_tables()
        for to in going_to:
            if to_data in to.text:
                to.click()
                break
        self.log.info("To location is placed")

    def calendar_click(self, date):
        self.calendars().click()

        calendartable = self.calendar_tables()
        for cal in calendartable:
            if cal.text == date:
                cal.click()
                break

        self.log.info("Date is placed")

    def search_button_click(self):
        self.search_button().click()
        self.log.info("Search button clicked")
        swf = showing_flights(self.driver)
        return swf

    def search_field(self, from_, from_data, to_, to_data, date):
        self.from_field(from_, from_data)
        self.to_field(to_, to_data)
        self.calendar_click(date)





