from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class base_class():

    def __init__(self, driver):
        self.driver = driver

    def login(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.CSS_SELECTOR, "button[type='button']").click()
        self.driver.find_element(By.XPATH, "//input[@placeholder='Enter your username']").send_keys("FPGNM4000027A")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']").send_keys("Flypigeon@123")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

    def webelement_click(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        elements = wait.until(ec.element_to_be_clickable((locator_type, locator)))
        return elements

    def find_webelements(self, locator_types, locators):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.presence_of_all_elements_located((locator_types, locators)))
        return element

    #dropdown
    def drop_down(self, locator_type, locator):
        dropdown = self.driver.find_element(locator_type, locator)
        drop = Select(dropdown)
        return drop