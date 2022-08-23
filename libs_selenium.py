from selenium.webdriver.chrome.options import Options
from selenium import webdriver

options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
url = 'https://github.com/'

def screenshot():
    # Navigate to github.com
    driver.get(url)

    # Extract the top heading from github.com
    text = driver.find_element_by_class_name('h000-mktg').text

    print(text)

    return text