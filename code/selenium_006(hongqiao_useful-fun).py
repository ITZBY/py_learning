from selenium_005(hongqiao_login) import hognqiao_login_base
from selenium_005(hongqiao_login) import EC
from selenium_005(hongqiao_login) import By
from selenium_005(hongqiao_login) import time

class housingList(hognqiao_login_base):
    def test_login(self):
        self.login(username="zby", password="test123456")