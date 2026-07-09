from login import selenium_login_base
from login import EC
from login import By
from login import time
from selenium.webdriver.common.action_chains import ActionChains
class Workbench(selenium_login_base):
    def test_login(self):
        self.login(tenatkey="danran", username="zbyzby", password="123456")
        print("登录成功!")
        
    def test_workbench(self,percent:float):
        self.wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div/div[2]/section/div/div/div/div[1]/div[1]/div[1]/a"))).click()
        time.sleep(5)
        self.wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div/div[2]/section/div/div/div/div[1]/div[1]/ul/li[1]"))).click()
        time.sleep(3)
        self.wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div[2]/section/div/div/div/div[1]/div[2]/div[1]/div[1]/div/input"))).click()
        print("点击新建审批-审批类型下拉成功")
        time.sleep(2)
        scroll_right = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".el-scrollbar__bar.is-vertical")))
        print("直接定位到整段滚动条,可获取百分比下拉幅度")
        time.sleep(2)
        script = """
        const bar = arguments[0];
        const percent = arguments[1];
        const dropdown = bar.closest('.el-select-dropdown');
        const scrollWrap = dropdown.querySelector('.el-select-dropdown__wrap');
        const maxScroll = scrollWrap.scrollHeight - scrollWrap.clientHeight;
        scrollWrap.scrollTop = maxScroll * percent;
        """
        self.driver.execute_script(script, scroll_right,percent)
        print("成功下拉")
        time.sleep(3)
        
        
        
        
        # 用来抓取短段滚动条，用像素计算拉动距离
        # ActionChains(self.driver).click_and_hold(scroll_right).move_by_offset(0,400).release().perform()
        # time.sleep(2)
        
        
        # 整个块滚动到像素单位下的位置
        # time.sleep(2)
        # Workbench_operate_type = self.wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div[1]")))
        # time.sleep(3)
        # ActionChains(self.driver).move_to_element(Workbench_operate_type).scroll_by_amount(0,400).perform()
        # time.sleep(5)
        # self.wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div[1]/div[1]/ul/li[15]"))).click()
        # time.sleep(5)
        # print("选则点击维修立项")
        
        
        
if __name__ == "__main__":
    test = Workbench()
    try:
        # 登录业务调用
        test.test_login()
        # 后续业务调用
        test.test_workbench(1)
        
    except Exception as e:
        print(f"测试失败{e}")
    finally:
        test.quie_browser()