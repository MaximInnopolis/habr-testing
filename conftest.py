import os
import shutil

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


print("Running conftest first")

@pytest.fixture(scope="session")
def driver_setup():
    global driver

    driver_path = ChromeDriverManager().install()
    chrome_service = Service(driver_path)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1420,1080')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    prefs = {"download.default_directory": os.getcwd()}
    chrome_options.add_experimental_option("prefs", prefs)

    chrome_executable_path = shutil.which("chrome") or shutil.which("chromium") or shutil.which("google-chrome")
    if chrome_executable_path is not None:
        chrome_options.binary_location = chrome_executable_path

    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    driver.maximize_window()

    yield driver
    driver.close()
    driver.quit()