from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
print("Testcase Started")

driver.maximize_window()
driver.get("https://www.linkedin.com/login")
driver.find_element_by_name("session_key").send_keys("username")
time.sleep(2)
driver.find_element_by_name("session_password").send_keys("Password")
time.sleep(2)
driver.find_element_by_class_name("btn__primary--large.from__button--floating").send_keys(Keys.ENTER)
time.sleep(10)
driver.close()
print("Testccase Compeleted")