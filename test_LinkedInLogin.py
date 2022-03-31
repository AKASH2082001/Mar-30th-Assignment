from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
print("Testcase Started")

driver.maximize_window()
driver.get("https://www.google.com/")
driver.find_element_by_name("q").send_keys("LinkedIn")
time.sleep(2)
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element_by_class_name("LC20lb.MBeuO.DKV0Md").click()
time.sleep(2)
driver.find_element_by_class_name("main__sign-in-link").click()
time.sleep(2)
driver.find_element_by_name("session_key").send_keys("9962873499")
time.sleep(2)
driver.find_element_by_name("session_password").send_keys("Pakash208")
time.sleep(2)
driver.find_element_by_class_name("btn__primary--large.from__button--floating").send_keys(Keys.ENTER)
time.sleep(10)
driver.close()
print("Testccase Compeleted")