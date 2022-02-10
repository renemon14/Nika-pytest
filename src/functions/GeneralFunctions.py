import logging

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager


class GeneralFunctions:

    driver = None
    timeWait = 30

    def open_browser(self, url, browser):

        if browser == "Chrome":
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--start-maximized')
            self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                           chrome_options=chrome_options)
            self.driver.get(url)
            return self.driver
        else:
            logging.error("[ERROR]: Browser not found")

    def implicit_wait_visible(self, locator):
        try:
            wait = WebDriverWait(self.driver, self.timeWait)
            wait.until(EC.visibility_of_element_located(locator))
            logging.info("[INFO]: Element Visible")

        except TimeoutException:
            raise ValueError("[ERROR]: Element NO visible")

    def implicit_wait_present(self, locator):
        try:
            wait = WebDriverWait(self.driver, self.timeWait)
            wait.until(EC.presence_of_element_located(locator))
            logging.info("[INFO]: Element present")

        except TimeoutException:
            raise ValueError("[ERROR]: Element NO present")

    def implicit_wait_clickable(self, locator):
        try:
            wait = WebDriverWait(self.driver, self.timeWait)
            wait.until(EC.element_to_be_clickable(locator))
            logging.info("[INFO]: Element clickable")

        except TimeoutException:
            raise ValueError("[ERROR]: Element NO clickable")

    def click_element(self, locator):
        try:
            self.implicit_wait_clickable(locator)
            self.driver.find_element(*locator).click()

        except:
            raise ValueError("[ERROR]: Element NO clickable")


    def send_key(self, locator, text):
        try:
            self.implicit_wait_visible(locator)
            element = self.driver.find_element(*locator)
            length =len(element.get_attribute('value'))
            element.send_keys(length * Keys.BACKSPACE)
            element.send_keys(text)
        except:
            raise ValueError("[ERROR]: No such element")

    def move_to_element(self, locator1, locator2):
        self.implicit_wait_present(locator1)
        self.implicit_wait_present(locator2)
        menu_element = self.driver.find_element(*locator1)
        submenu_element = self.driver.find_element(*locator2)
        build = ActionChains(self.driver)
        build.move_to_element(menu_element).click(submenu_element).perform()
