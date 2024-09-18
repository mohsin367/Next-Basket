import time

import pyautogui
import pytest
from selenium import webdriver


def browser_open():
    pyautogui.hotkey('win')
    time.sleep(.5)
    pyautogui.write('cmd')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write('cd "C:\Program Files\Google\Chrome\Application"')
    pyautogui.press('enter')
    pyautogui.write('chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\Chromedata"')
    pyautogui.press('enter')
    pyautogui.write('exit')
    pyautogui.press('enter')


# browser_open()
# options = Options()
# options.add_experimental_option("debuggerAddress", "localhost:9222")
# options.add_argument("--start-maximized")
# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()


@pytest.fixture()
def setup(request):
    driver.maximize_window()
    yield driver