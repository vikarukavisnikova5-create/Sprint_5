
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--window-size=1600,900")

driver = webdriver.Chrome(options=options)

driver.get("https://stellarburgers.education-services.ru/")
time.sleep(100)