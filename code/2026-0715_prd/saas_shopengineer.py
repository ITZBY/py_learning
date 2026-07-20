from saas_login import saas_login_base
from saas_login import By
from saas_login import EC
from saas_login import time

class shopEngineer(saas_login_base):
    def test_login(self):
        self.login(tenatkey="danran", username="zbyzby", password="123456")
        print("login_successed!")
        time.sleep(3)
    def test_export(self):
        # 点击效果：从工作台->点击项目管理->点击工程条件->点击房源工程条件
        self.wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div/div[2]/aside/ul[1]/li[2]/div/div"))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div/div[2]/aside/ul[1]/li[2]/ul/li[4]"))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div/div[2]/section/div/div/div/ul/li[2]/span"))).click()
        print("跳转到房源工程条件tab")
        time.sleep(3)
    
if __name__ == "__main__":
    test = shopEngineer()
    try:
        test.test_login()
        test.test_export()
    except Exception as e:
        print(f"登录失败{e}")
    finally:
        test.quie_browser()