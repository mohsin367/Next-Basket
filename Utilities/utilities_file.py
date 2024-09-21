import os
import random
import time
import allure
import pyautogui
from datetime import datetime
from selenium.common import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from Object.locators import App_Data
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Baseclass:
    def _init_(self, driver):
        self.driver = driver

    @staticmethod
    def take_ss(driver):
        allure.attach(driver.get_screenshot_as_png(), name="screenshot",
                      attachment_type=allure.attachment_type.PNG)

    @staticmethod
    def select_and_remove():
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')


    @staticmethod
    def time_rn():
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        return f'---- timestamp: {current_time}'



    @staticmethod
    def xpath_click(driver, path):
        driver.find_element(By.XPATH, path).click()

    @staticmethod
    def xpath_send_keys(driver, path, value):
        driver.find_element(By.XPATH, path).send_keys(value)


    @staticmethod
    def xpath_is_displayed(driver, path):
        driver.find_element(By.XPATH, path).is_displayed()

    @staticmethod
    def xpath_is_displayed_with_ss(driver, path):
        try:
            driver.find_element(By.XPATH, path).is_displayed()
        except NoSuchElementException:
            Baseclass.take_ss(driver)
            assert False

    @staticmethod
    def xpath_is_displayed_with_while(driver, path):
        while 1 == 1:
            try:
                driver.find_element(By.XPATH, path).is_displayed()
                break
            except NoSuchElementException:
                time.sleep(1)

    @staticmethod
    def xpath_get_text(driver, path):
        e_text = driver.find_element(By.XPATH, path).text
        return e_text

    @staticmethod
    def xpath_value_check(driver, path):
        driver.find_element(By.XPATH, path)

    @staticmethod
    def scroll_to_location(driver, path):
        js_code = "arguments[0].scrollIntoView();"
        element = driver.find_element(By.XPATH, path)
        driver.execute_script(js_code, element)

    @staticmethod
    def after_scroll_xpath_click(driver, path):
        button = driver.find_element(By.XPATH, path)
        driver.execute_script("arguments[0].click();", button)


    @staticmethod
    def explicit_wait_to_be_visible(driver, timeout, path):
        element = WebDriverWait(driver, int(timeout)).until(
            EC.presence_of_element_located((By.XPATH, path))
        )
        element.is_displayed()

    @staticmethod
    def loading_wait(driver, sec=None):
        time.sleep(sec)
        while 1 == 1:
            try:
                Baseclass.xpath_is_displayed(driver, App_Data.Value['loading_screen_wait'])
            except NoSuchElementException:
                break

    @staticmethod
    def stop_check():
        pyautogui.alert(text='Stopped! Please check.')


    @staticmethod
    def check_element_exist_then_wait_while(driver, path):
        while 1 == 1:
            try:
                Baseclass.xpath_is_displayed(driver, path)
                time.sleep(1)
            except NoSuchElementException:
                break

    @staticmethod
    def try_except_click(driver, path1, path2):
        try:
            Baseclass.xpath_click(driver, path1)
        except NoSuchElementException:
            Baseclass.xpath_click(driver, path2)