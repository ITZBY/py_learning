from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
driver_path = "D:/Download/chromedriver-win64/chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)


driver.get("http://192.168.1.186:81/#/login")
driver.maximize_window() #使用最大化可避免找不到元素
input_Element = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/form/div/div[1]/div/div/input").send_keys("danran")
input_Element = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/form/div/div[2]/div/div/input").send_keys("zbyzby")
input_Element = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/form/div/div[3]/div/div/input").send_keys("123456")
input_Element = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/form/div/label[2]/span[1]").click()
input_Element = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/form/div/div[5]").click()
time.sleep(3)
input_Element = driver.find_element(By.XPATH,"/html/body/div/div/div[1]/div[3]/div/div[1]/div/i").click()
time.sleep(1)
input_Element = driver.find_element(By.XPATH,"/html/body/div/div/div[1]/div[3]/div/div[1]/div/div[1]/input").send_keys("合同")
time.sleep(3)
input_Element = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[3]/div/div[1]/div/div[2]/div/div[1]/div[1]").click()
time.sleep(2)
input_Element = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[3]/div/div[1]/div/div[4]/div[1]/div[2]/div[1]/div[2]/div[1]/ul/li[2]").click()
time.sleep(3)
input_Element = driver.find_element(By.XPATH,"/html/body/div/div/div[1]/div[3]/div/div[1]/div/div[4]/div[1]/div[2]/div[1]/div[1]/i").click()
time.sleep(5)
driver.quit()