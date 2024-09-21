import os
import time

import pyautogui
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from Object.locators import App_Data
from Utilities.utilities_file import Baseclass
from Testcases.purchase import Purchase_items

class TestWebsiteBasket:
    def test_website_launch(self, setup):
        self.driver = setup
        Purchase_items.open_site(self.driver, setup)

    def home_page_assertion(self, setup):
        self.driver = setup
        Purchase_items.home_page_check(self.driver)

    def test_select_product(self, setup):
        self.driver = setup
        Purchase_items.select_non_promo_product(self.driver)