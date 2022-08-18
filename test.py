import time
from selenium import webdriver
from PIL import Image
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--start-maximized')


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
driver.maximize_window()
driver.get("https://zing.vn")
time.sleep(5)

#the element with longest height on page
total_width = driver.execute_script('return document.body.parentNode.scrollWidth')
total_height = driver.execute_script("return document.body.parentNode.scrollHeight")

driver.set_window_size(1920, total_height)      #the trick
time.sleep(5)
driver.save_screenshot("screenshot1.png")

screenshot = Image.open("screenshot1.png")
screenshot.show()

driver.quit()