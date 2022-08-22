# from flask import Flask
# import time
# from selenium import webdriver
# from PIL import Image
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options

# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--start-maximized')

# # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
# driver = webdriver.Chrome(service=ChromeService("/usr/src/app/chromedriver"), options=chrome_options)
# driver.maximize_window()

# app = Flask(__name__)
# app.debug = True

# @app.route('/')
# def index():
#     driver.get("https://zing.vn")
#     time.sleep(5)

#     total_width = driver.execute_script('return document.body.parentNode.scrollWidth')
#     total_height = driver.execute_script("return document.body.parentNode.scrollHeight")

#     driver.set_window_size(1920, total_height)
#     time.sleep(5)

#     file_name = "screenshot1.png"
#     driver.save_screenshot(file_name)

#     screenshot = Image.open(file_name)
#     screenshot.show()

#     driver.quit()
#     return True

# app.run(host='0.0.0.0', port='80')