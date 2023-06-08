import time

import pytest
import softest

import logging

from selenium.webdriver.common.by import By

from pages.flights.oneway import oneway
from utilities.utils import Utils


@pytest.mark.usefixtures("setup")
class Test_FLight_Booking(softest.TestCase):
    log = Utils.custom_logger()

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.one = oneway(self.driver)


    def test_flight_ticket_book(self):
        self.one.login()
        self.one.search_field("hyde", "HYD", "Delhi", "DEL", "5")
        
        swf = self.one.search_button_click()
        #time.sleep(5)

        expected_text = "Showing best flights"
        real_text = swf.showing_flights_data().text

        self.soft_assert(self.assertEqual, expected_text, real_text)

        if real_text == expected_text:
            self.log.debug("test is passed")
        else:
            self.log.debug("test is failed")

        pd = swf.booknow_button_click()

        pd.proceed_button_click()
        pd.passenger_details("8639643224", "sasikumar@mailinator.com", "Mrs")
        time.sleep(3)

        self.assert_all()

    def test_demo(self):

        self.driver.find_element(By.XPATH, "//div[@class='nav-logo']//div//img[@alt='flypigeon']")
        self.one.search_field("hyde", "HYD", "Delhi", "DEL", "5")

        swf = self.one.search_button_click()


