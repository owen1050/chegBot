from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
#chrome_options.add_argument('--headless')
chrome_options.add_argument("--enable-javascript")

#"S:\Downloads\Licence and SS.pdf"
driver = webdriver.Chrome(chrome_options = chrome_options, executable_path= "S:\\Downloads\\chromedriver_win32\\chromedriver.exe") #C:\\Users\\Owen1\\Downloads\\chromedriver_win32/chromedriver.exe')
driver.get("https://www.chegg.com/auth?action=login")

user = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/div[2]/div/div[2]/div/oc-component/div[2]/div/div/div[2]/div[1]/div[1]/div/form/div/div/div/div/div[1]/input')
user.send_keys("will1050will@gmail.com")
password = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/div[2]/div/div[2]/div/oc-component/div[2]/div/div/div[2]/div[1]/div[1]/div/form/div/div/div/div/div[3]/input')
password.send_keys("SolarCarS3")
python_button = driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/div[2]/div/div[2]/div/oc-component/div[2]/div/div/div[2]/div[1]/div[1]/div/form/div/div/div/footer/button")
python_button.click()

driver.get("https://www.chegg.com/homework-help/questions-and-answers/ap-physics-1-kinematics-il-review-quiz-1-airplane-flying-horizontally-velocity-500m-s-alti-q48666202?cs_resub=1")
height = driver.execute_script("return document.body.scrollHeight")
print(height)

if(True):
    driver.set_window_size(1920, 2000)      #the trick
    time.sleep(2)
    driver.save_screenshot("screenshot1.png")
    python_button = driver.find_element_by_xpath("/html/body/div[1]/main/div[1]/section[1]/div/button")
    python_button.click()
