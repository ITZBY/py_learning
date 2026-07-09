from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
driver_path = "D:/Download/chromedriver-win64/chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

driver.get("http://192.168.1.186:81/#/login")
driver.maximize_window()
input_Element = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/form/div/div[1]/div/div/input").send_keys("danran")
input_Element = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/form/div/div[2]/div/div/input").send_keys("zbyzby")
input_Element = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/form/div/div[3]/div/div/input").send_keys("123456")
input_Element = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/form/div/label[2]/span[1]").click()
input_Element = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/form/div/div[5]").click()
time.sleep(3)
input_Element_scroll = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/section/div/div/div/div[1]")
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;",input_Element_scroll)
driver.execute_script("arguments[0].scrollTop = 2000;",input_Element_scroll)
time.sleep(5)
# 将滚动效果定位到租赁房源
input_Element_scroll_zl = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/section/div/div/div/div[1]/div[3]/div[1]/div/div/div[21]")
driver.execute_script("arguments[1].scrollIntoView({block:'center'});",input_Element_scroll,input_Element_scroll_zl)
time.sleep(5)

input_Element_right_scroll = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/section/div/div/div/div[2]")
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;",input_Element_right_scroll)
driver.execute_script("arguments[0].scrollTop = 100;",input_Element_right_scroll)
time.sleep(5)
# 将右侧滚动到日期展示处
input_Element_right_scroll_rq = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/section/div/div/div/div[2]/div[3]/micro-app/micro-app-body/div/div/div/div[6]/div[2]")
driver.execute_script("arguments[1].scrollIntoView({block:'center'});",input_Element_right_scroll,input_Element_right_scroll_rq)
time.sleep(5)
driver.quit()