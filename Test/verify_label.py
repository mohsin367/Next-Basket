import os
import time

import pyautogui
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from Object.objects import App_Data
from Utilities.utilities_file import Baseclass
from Testcases.purchase import Purchase_items

class VerifyLabel:
    def test_website_launch(self, setup):
        self.driver = setup
        Purchase_items.open_site(self.driver, setup)

    def test_verify_label(self, setup):
        self.driver = setup
        Purchase_items.verify_off_label(self.driver)