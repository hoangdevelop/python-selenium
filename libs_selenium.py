from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--headless")
# options.add_argument("window-size=1400,1500")
# options.add_argument("--disable-gpu")
# options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
# options.add_argument("enable-automation")
# options.add_argument("--disable-infobars")
# options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

def screenshot_full_page(url):
    # Navigate to github.com
    driver.get(url)

    original_size = driver.get_window_size()
    # required_width = driver.execute_script('return document.body.parentNode.scrollWidth')
    required_height = driver.execute_script('return document.body.parentNode.scrollHeight')
    driver.set_window_size(1920, required_height)
    # driver.save_screenshot(path)  # has scrollbar

    # WebDriverWait(driver, 10).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')


    driver.find_element(By.TAG_NAME, 'body').screenshot('./screenshot.png')  # avoids scrollbar
    driver.set_window_size(original_size['width'], original_size['height'])

