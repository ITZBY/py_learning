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
        self.wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div[2]/section/div/div/div/div[1]/span/div[1]/div"))).click()
        print("1")
        scroll_container = self.wait.until(EC.presence_of_element_located((By.XPATH,'//div[contains(@class,"el-select-dropdown__wrap")]')))
        print("2")
        last_scroll_Height = 0
        while True:
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;",scroll_container)
            new_scroll_height = self.driver.execute_script("return arguments[0].scrollHeight;",scroll_container)
            if new_scroll_height ==last_scroll_Height:
                break
            last_scroll_Height = new_scroll_height
        target_text = "黄浦江园区（"
        target_li = self.wait.until(EC.presence_of_element_located((By.XPATH,f'//li[contains(@class,"el-select-dropdown__item") and normalize-space()="{target_text}"]')))
        self.driver.execute_script("arguments[0].scrollIntoView(true);",target_li)
        self.wait.until(EC.element_to_be_clickable(target_li)).click()
        
        
        time.sleep(6)
        print("按照筛选条件查询列表数据")
if __name__ == "__main__":
    test = shopEngineer()
    try:
        test.test_login()
        test.test_export()
    except Exception as e:
        print(f"登录失败{e}")
    finally:
        test.quie_browser()