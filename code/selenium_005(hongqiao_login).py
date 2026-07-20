from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

driver_path = "D:/Download/chromedriver-win64/chromedriver.exe"
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)
driver.get("http://192.168.1.140/#/login")
driver.maximize_window()
login_username = driver.find_element(By.XPATH,"/html/body/div/div/div/form/div/div[2]/div/div/input").send_keys("zby")
login_password = driver.find_element(By.XPATH,"/html/body/div/div/div/form/div/div[3]/div/div/input").send_keys("test123456")
login_agree = driver.find_element(By.XPATH,"/html/body/div/div/div/form/div/label[2]/span[1]/span").click()
login_click = driver.find_element(By.XPATH,"/html/body/div/div/div/form/div/div[5]").click()
print("login_success!")
time.sleep(5)
driver.quit()