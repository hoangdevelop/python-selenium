from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from threading import Thread
load_dotenv()
BROWSERSTACK_USERNAME = os.environ.get("BROWSERSTACK_USERNAME") or "BROWSERSTACK_USERNAME"
BROWSERSTACK_ACCESS_KEY = os.environ.get("BROWSERSTACK_ACCESS_KEY") or "BROWSERSTACK_ACCESS_KEY"
URL = os.environ.get("URL") or "https://hub.browserstack.com/wd/hub"
BUILD_NAME = "browserstack-build-1"
capabilities = [
    {
        "browserName": "chrome",
        "browserVersion": "67.0",
        "os": "OS X",
        "osVersion": "Mavericks",
        "sessionName": "BStack Python sample parallel",
        "buildName": BUILD_NAME,
    },
]
def get_browser_option(browser):
    switcher = {
        "chrome": ChromeOptions(),
        "firefox": FirefoxOptions(),
        "edge": EdgeOptions(),
        "safari": SafariOptions(),
    }
    return switcher.get(browser, ChromeOptions())
def run_session(cap):
    bstack_options = {
        # "osVersion" : "15",
        # "deviceName" : "iPhone 13 Pro Max",
        # "realMobile" : "false",
        "userName": BROWSERSTACK_USERNAME,
        "accessKey": BROWSERSTACK_ACCESS_KEY
    }
    # if "os" in cap:
    #   bstack_options["os"] = cap["os"]
    options = get_browser_option(cap["browserName"].lower())
    # if "browserVersion" in cap:
    #   options.browser_version = cap["browserVersion"]

    mobile_emulation = {"deviceName": "iPhone X"}
    options.add_experimental_option("mobileEmulation", mobile_emulation)

    options.set_capability('bstack:options', bstack_options)
    driver = webdriver.Remote(
        command_executor=URL,
        options=options)
    try:
        # driver.maximize_window()
        driver.get("https://zing.vn/")
        WebDriverWait(driver, 1).until(EC.title_contains("Zing"))

        original_size = driver.get_window_size()
        # total_width = driver.execute_script('return document.body.parentNode.scrollWidth')
        total_height = driver.execute_script("return document.body.parentNode.scrollHeight")

        # driver.set_window_size(1920, total_height)
        driver.set_window_size(original_size['width'], total_height)

        file_name = "screenshot1.png"
        driver.save_screenshot(file_name)
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "iPhone 12 has been successfully added to the cart!"}}')
    except NoSuchElementException:
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Some elements failed to load"}}')
    except Exception:
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Some exception occurred"}}')
    # Stop the driver
    driver.quit()
for cap in capabilities:
  Thread(target=run_session, args=(cap,)).start()