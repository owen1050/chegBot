from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(chrome_options = chrome_options, executable_path='C:\\Users\\Owen1\\Downloads\\chromedriver_win32/chromedriver.exe')
driver.get("http://www.google.com")

driver.set_window_size(1920, 2000)      #the trick
time.sleep(2)
driver.save_screenshot("screenshot1.png")
driver.quit()