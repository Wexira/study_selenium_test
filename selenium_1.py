import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdrive.common.by import By

"""Запуск webdriver"""
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

"""Авторизация"""
login_problem_user = "problem_user"
password_all = "secret_sauce"

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_problem_user)
print("Input Login")
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(login_problem_user)
print("Input Password")
button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
print("Click Button Login")


"""Info Product #1"""
product_1 = driver.find_element(By.XPATH, "//input[@id='item_0_title_link']")
value_product_1 = product_1.text
print(value_product_1)

price_product_1 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div")
value_price_product_1 = price_product_1.text
print(value_price_product_1)
time.sleep(2)

select_product_1 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']")
select_product_1.click()
print(select_product_1)
time.sleep(2)

"""Info Product #2"""
product_2 = driver.find_element(By.XPATH, "//input[@id='item_5_title_link']")
value_product_2 = product_2.text
print(value_product_1)

price_product_2 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div")
value_price_product_2 = price_product_2.text
print(value_price_product_2)
time.sleep(2)

select_product_2 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']")
select_product_2.click()
print(select_product_2)
time.sleep(2)





