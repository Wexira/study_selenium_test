from selenium.webdriver.support.wait import WebDriverWait

from Login_page import LoginPage
from logout import Logout


class Test:
    def test_select_product(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        g = Service()
        driver = webdriver.Chrome(options=options, service=g)
        base_url = 'https://www.saucedemo.com/'
        driver.get(base_url)
        driver.maximize_window()

        print("Start Test")
        list_users = ["standard_user", "locked_out_user", "problem_user", "performance_glitch_user",
                      "error_user", "visual_user"]
        login = LoginPage(driver)
        for user in list_users:
            try:
                login.authorization(user, login_password="secret_sauce")
                time.sleep(10)
                success_test = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='title']")))
                value_success_test = success_test.text
                assert value_success_test == "Products"
                print("Test Success!!!")
                back_to_page = Logout(driver)
                back_to_page.button_burger()
                back_to_page.logout()
            except:
                error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='login_button_container'] /div/form/div[3] /h3")))
                value_error_message = error_message.text
                print(value_error_message)
                if value_error_message == "Epic sadface: Sorry, this user has been locked out.":
                    print("Этот пользователь заблокирован")
                driver.refresh()
                time.sleep(3)


test = Test()
test.test_select_product()
