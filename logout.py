import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Logout:
    def __init__(self, driver):
        self.driver = driver

    """"Вызов бокового меню"""

    def button_burger(self):
        sidebar_menu = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='react-burger-menu-btn']")))
        sidebar_menu.click()
        print("Click Sidebar Menu")
        time.sleep(5)

    """"Возрат на стартовую страницу"""

    def logout(self):
        sidebar_logout = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@id='logout_sidebar_link']")))
        sidebar_logout.click()
        print("Click Sidebar Logout")
