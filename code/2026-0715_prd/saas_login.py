from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

class saas_login_base():
    def __init__(self):
        # 添加驱动
        driver_path = "D:/Download/chromedriver-win64/chromedriver.exe"
        service = Service(executable_path=driver_path)
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver,10)
    def login(self, tenatkey:str, username:str, password:str):
        # 登录
        self.driver.get("http://192.168.1.186:81/#/login")
        self.driver.maximize_window()
        self.wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/form/div/div[1]/div/div/input"))).send_keys(tenatkey)
        self.wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/form/div/div[2]/div/div/input"))).send_keys(username)
        self.wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/form/div/div[3]/div/div/input"))).send_keys(password)
        self.wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/form/div/label[2]/span[1]"))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div[2]/div/div[2]/form/div/div[5]"))).click()
        # print("login success!")
        time.sleep(5)
    def quie_browser(self):
        self.driver.quit()


""" 单独测试登录效果
if __name__ == "__main__":
    test = saas_login_base()
    try:
    # 登录业务调用
        test.login(tenatkey="danran", username="zbyzby", password="123456")
    except Exception as e:
        print(f"测试失败{e}")
    finally:
        test.quie_browser()
"""

