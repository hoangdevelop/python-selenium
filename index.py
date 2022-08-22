
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

# URL = "http://localhost:4444/wd/hub"
# URL = "https://hub.browserstack.com/wd/hub"
URL = "https://hub-cloud.browserstack.com/wd/hub"
BUILD_NAME = "browserstack-build-1"
BROWSERSTACK_USERNAME = "minhhongnguyn_x2NoZq"
BROWSERSTACK_ACCESS_KEY = "hGFHt8x7nckhLJqkYHhe"

capabilities = [
    # {
    #     "browserName": "safari",
    #     "browserVersion": "15.3",
    #     "os": "OS X",
    #     "osVersion": "Monterey",
    #     "sessionName": "BStack Python sample parallel", # test name
    #     "buildName": BUILD_NAME,  # Your tests will be organized within this build
    # },
    {
        "browserName": "android",
        "deviceName": "Samsung Galaxy S7",
        "osVersion": "6.0",
        "sessionName": "BStack Python sample parallel", # test name
        "buildName": BUILD_NAME,  # Your tests will be organized within this build
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
        "osVersion" : cap["osVersion"],
        "buildName" : cap["buildName"],
        "sessionName" : cap["sessionName"],
        "userName": BROWSERSTACK_USERNAME,
        "accessKey": BROWSERSTACK_ACCESS_KEY
    }
    if "os" in cap:
      bstack_options["os"] = cap["os"]

    options = get_browser_option(cap["browserName"].lower())

    if "browserVersion" in cap:
      options.browser_version = cap["browserVersion"]

    options.set_capability('bstack:options', bstack_options)
    driver = webdriver.Remote(
        command_executor=URL,
        options=options)
    try:
        driver.maximize_window()
        driver.get("https://zing.vn/")
        WebDriverWait(driver, 10).until(EC.title_contains("Zing"))

        # total_width = driver.execute_script('return document.body.parentNode.scrollWidth')
        # total_height = driver.execute_script("return document.body.parentNode.scrollHeight")

        # driver.set_window_size(1920, total_height)

        file_name = "screenshot1.png"
        driver.save_screenshot(file_name)

        print("Test Execution Successfully Completed!")
    except Exception:
        print("Some exception occurred")

    driver.quit()
for cap in capabilities:
  Thread(target=run_session, args=(cap,)).start()