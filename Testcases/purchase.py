import os
import time
import pyautogui
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from Object.locators import App_Data
from Utilities.utilities_file import Baseclass


class Purchase_items:
    def _init_(self, driver):
        self.driver = driver

    def open_site(self, setup):
        self.driver = setup
        self.driver.get(App_Data.auth_url)
        time.sleep(1.5)

    def home_page_check(self):
        try:
            cookie_button = self.driver.find_element(By.XPATH, App_Data.Value['accept_cookies'])
            cookie_button.click()
            print('test')
            self.driver.find_element(By.XPATH, App_Data.Value['Homepage-heading']).is_displayed()
            if Baseclass.xpath_get_text(self.driver, App_Data.Value['Homepage-heading']) == 'New':
                pass
            assert True
        except NoSuchElementException:
            Baseclass.take_ss(self.driver)
            assert False

    def select_non_promo_product(self):     # complete product selection process
        element_visible = False
        while not element_visible:
            try:

                element = self.driver.find_element(By.XPATH,App_Data.Value['select_product'])
                if element.is_displayed():
                    element_visible = True
                    product_click = self.driver.find_element(By.XPATH, App_Data.Value['click_product'])
                    product_click.click()
                    button_click = self.driver.find_element(By.XPATH, App_Data.Value['add_cart'])
                    button_click.click()
                    pop_up = self.driver.find_element(By.XPATH, App_Data.Value['pop_up'])
                    pop_up.click()
                    basket = self.driver.find_element(By.XPATH, App_Data.Value['basket'])
                    basket.click()
                    check_out = self.driver.find_element(By.XPATH, App_Data.Value['check_out'])
                    check_out.click()
            except NoSuchElementException:
                print("Element not found, retrying...")


    def verify_off_label(self):
        element_visible = False
        while not element_visible:
            try:
                self.driver.find_element(By.XPATH, App_Data.Value['off_label']).is_displayed()
                element_visible = True
                pass
                assert True
            except NoSuchElementException:
                Baseclass.take_ss(self.driver)
                assert False