class Product():
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def description_product(self):
        name = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
        price = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
        # product = product.text
        # value_price_product = price_product.text
        
    def select_products(self):
        select_product_1 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
        select_product_2 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
        select_product_3 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
        select_product_4 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
        select_product_5 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
        select_product_6 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")

        
    def cart_product(self):
        cart_product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
        value_cart_product_1 = cart_product_1.text
        print(value_cart_product_1)
        assert number1 == value_cart_product_1
        print("INFO Cart Product 1 GOOD")
        # проверка на соответствие названия товара на главной странице товару в корзине
        """INFO Cart Product #1"""
        cart_product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
        value_cart_number1 = cart_product_1.text
        print(value_cart_number1)
        assert number1 == value_cart_product_1
        print("INFO Cart Product 1 GOOD")
        # проверка на соответствие названия товара на главной странице товару в корзине
        price_cart_product = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
        value_cart_price_product = price_cart_product.text
        print(value_cart_price_product)
        assert value_price_number1 == value_cart_price_product
        print("INFO Price Cart Product 1 GOOD")
        button_checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
        button_checkout.click()
        print("Click Checkout")
        time.sleep(2)
        
    def user_info(self):
        """"Select User INFO"""
        first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
        first_name.send_keys("Lana")
        print("Input First Name")
        time.sleep(2)
        last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
        last_name.send_keys("Sokol")
        print("Input Last Name")
        time.sleep(2)
        zip_code = driver.find_element(By.XPATH, "//input[@id='postal-code']")
        zip_code.send_keys("1234")
        print("Input Zip code")
        time.sleep(2)
        button_continue = driver.find_element(By.XPATH, "//input[@id='continue']")
        button_continue.click()
        print("Click Continue button")

    def cart(self):
        cart = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
        cart.click()
        print("Enter Cart")
        time.sleep(2)
        
    def finish_product(self):
        """"INFO Finish Product #1"""
        finish_product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
        value_finish_product_1 = finish_product_1.text
        print(value_finish_product_1)
        assert number1 == value_finish_product_1
        print("INFO finish Product 1 GOOD")
        # проверка на соответствие названия товара на главной странице товару в корзине
        price_finish_product = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
        value_finish_price_product = price_finish_product.text
        print(value_finish_price_product)
        assert value_price_number1 == value_finish_price_product
        print("INFO Price finish Product 1 GOOD")
        summary_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[6]")
        value_summary_price = summary_price.text
        print(value_summary_price)
        item_total = "Item total: " + value_finish_price_product
        print(item_total)
        assert value_summary_price == item_total
        print("Total summary price Good")
        # Возврат на страницу каталога
        button_finish = driver.find_element(By.XPATH, "//button[@id='finish']")
        button_finish.click()
        print("Click Button Finish")
        button_back_home = driver.find_element(By.XPATH, "//button[@id ='back-to-products']")
        button_back_home.click()
        print("Click Button Back Home")
        elif products == 2:
            print(number2)
            """"INFO Product #2"""
            product_2 = driver.find_element(By.XPATH, "//a[@id='item_0_title_link']")
            number2 = product_2.text
            print(number2)
            price_product_2 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div")
            value_price_number2 = price_product_2.text
            print(value_price_number2)
            time.sleep(2)
            select_product_2 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']")
            select_product_2.click()
            print("Click select product 2")
            time.sleep(2)
            cart = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
            cart.click()
            print("Enter Cart")
            time.sleep(2)
            """INFO Cart Product #2"""
            cart_product_2 = driver.find_element(By.XPATH, "//a[@id='item_0_title_link']")
            value_cart_product_2 = cart_product_2.text
            print(value_cart_product_2)
            assert number2 == value_cart_product_2
            print("INFO Cart Product 2 GOOD")
            # проверка на соответствие названия товара на главной странице товару в корзине
            """INFO Cart Product #2"""
            cart_product_2 = driver.find_element(By.XPATH, "//a[@id='item_0_title_link']")
            value_cart_number2 = cart_product_2.text
            print(value_cart_number2)
            assert number2 == value_cart_product_2
            print("INFO Cart Product 2 GOOD")
            # проверка на соответствие названия товара на главной странице товару в корзине
            price_cart_product = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
            value_cart_price_product = price_cart_product.text
            print(value_cart_price_product)
            assert value_price_number2 == value_cart_price_product
            print("INFO Price Cart Product 2 GOOD")
            button_checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
            button_checkout.click()
            print("Click Checkout")
            time.sleep(2)
            """"Select User INFO"""
            first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
            first_name.send_keys("Lana")
            print("Input First Name")
            time.sleep(2)
            last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
            last_name.send_keys("Sokol")
            print("Input Last Name")
            time.sleep(2)
            zip_code = driver.find_element(By.XPATH, "//input[@id='postal-code']")
            zip_code.send_keys("1234")
            print("Input Zip code")
            time.sleep(2)
            button_continue = driver.find_element(By.XPATH, "//input[@id='continue']")
            button_continue.click()
            print("Click continue button")
            """"INFO Finish Product #2"""
            finish_product_2 = driver.find_element(By.XPATH, "//a[@id='item_0_title_link']")
            value_finish_product_2 = finish_product_2.text
            print(value_finish_product_2)
            assert number2 == value_finish_product_2
            print("INFO finish Product 2 GOOD")
            # проверка на соответствие названия товара на главной странице товару в корзине
            price_finish_product = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
            value_finish_price_product = price_finish_product.text
            print(value_finish_price_product)
            assert value_price_number2 == value_finish_price_product
            print("INFO Price finish Product 2 GOOD")
            summary_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[6]")
            value_summary_price = summary_price.text
            print(value_summary_price)
            item_total = "Item total: " + value_finish_price_product
            print(item_total)
            assert value_summary_price == item_total
            print("Total summary price Good")
            # Возврат на страницу каталога
            button_finish = driver.find_element(By.XPATH, "//button[@id='finish']")
            button_finish.click()
            print("Click Button Finish")
            button_back_home = driver.find_element(By.XPATH, "//button[@id ='back-to-products']")
            button_back_home.click()
            print("Click Button Back Home")
        elif products == 3:
            print(number3)
            """"INFO Product #3"""
            product_3 = driver.find_element(By.XPATH, "//a[@id='item_1_title_link']")
            number3 = product_3.text
            print(number3)
            price_product_3 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[3]/div[2]/div[2]/div")
            value_price_number3 = price_product_3.text
            print(value_price_number3)
            time.sleep(2)
            select_product_3 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
            select_product_3.click()
            print("Click select product 3")
            time.sleep(2)
            cart = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
            cart.click()
            print("Enter Cart")
            time.sleep(2)
            """INFO Cart Product #3"""
            cart_product_3 = driver.find_element(By.XPATH, "//a[@id='item_1_title_link']")
            value_cart_product_3 = cart_product_3.text
            print(value_cart_product_3)
            assert number3 == value_cart_product_3
            print("INFO Cart Product 3 GOOD")
            # проверка на соответствие названия товара на главной странице товару в корзине
            """INFO Cart Product #3"""
            cart_product_3 = driver.find_element(By.XPATH, "//a[@id='item_1_title_link']")
            value_cart_number3 = cart_product_3.text
            print(value_cart_number3)
            assert number3 == value_cart_product_3
            print("INFO Cart Product 3 GOOD")
            # проверка на соответствие названия товара на главной странице товару в корзине
            price_cart_product = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
            value_cart_price_product = price_cart_product.text
            print(value_cart_price_product)
            assert value_price_number3 == value_cart_price_product
            print("INFO Price Cart Product 3 GOOD")
            button_checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
            button_checkout.click()
            print("Click Checkout")
            time.sleep(2)
            """"Select User INFO"""
            first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
            first_name.send_keys("Lana")
            print("Input First Name")
            time.sleep(2)
            last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
            last_name.send_keys("Sokol")
            print("Input Last Name")
            time.sleep(2)
            zip_code = driver.find_element(By.XPATH, "//input[@id='postal-code']")
            zip_code.send_keys("1234")
            print("Input Zip code")
            time.sleep(2)
            button_continue = driver.find_element(By.XPATH, "//input[@id='continue']")
            button_continue.click()
            print("Click continue button")
            """"INFO Finish Product #3"""
            finish_product_3 = driver.find_element(By.XPATH, "//a[@id='item_1_title_link']")
            value_finish_product_3 = finish_product_3.text
            print(value_finish_product_3)
            assert number3 == value_finish_product_3
            print("INFO finish Product 3 GOOD")
            # проверка на соответствие названия товара на главной странице товару в корзине
            price_finish_product = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
            value_finish_price_product = price_finish_product.text
            print(value_finish_price_product)
            assert value_price_number3 == value_finish_price_product
            print("INFO Price finish Product 3 GOOD")
            summary_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[6]")
            value_summary_price = summary_price.text
            print(value_summary_price)
            item_total = "Item total: " + value_finish_price_product
            print(item_total)
            assert value_summary_price == item_total
            print("Total summary price Good")
            # Возврат на страницу каталога
            button_finish = driver.find_element(By.XPATH, "//button[@id='finish']")
            button_finish.click()
            print("Click Button Finish")
            button_back_home = driver.find_element(By.XPATH, "//button[@id ='back-to-products']")
            button_back_home.click()
            print("Click Button Back Home")
        elif products == 4:
            print(number4)
            """"INFO Product #4"""
            product_4 = driver.find_element(By.XPATH, "//a[@id='item_5_title_link']")
            number4 = product_4.text
            print(number4)
            price_product_4 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[4]/div[2]/div[2]/div")
            value_price_number4 = price_product_4.text
            print(value_price_number4)
            time.sleep(2)

            select_product_4 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']")
            select_product_4.click()
            print("Click select product 4")
            time.sleep(2)

            cart = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
            cart.click()
            print("Enter Cart")
            time.sleep(2)
            """INFO Cart Product #4"""
            cart_product_4 = driver.find_element(By.XPATH, "//a[@id='item_5_title_link']")
            value_cart_product_4 = cart_product_4.text
            print(value_cart_product_4)
            assert number4 == value_cart_product_4
            print("INFO Cart Product 4 GOOD")

            # проверка на соответствие названия товара на главной странице товару в корзине
            price_cart_product = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
            value_cart_price_product = price_cart_product.text
            print(value_cart_price_product)
            assert value_price_number4 == value_cart_price_product
            print("INFO Price Cart Product 4 GOOD")
            button_checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
            button_checkout.click()
            print("Click Checkout")
            time.sleep(2)

            """"Select User INFO"""
            first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
            first_name.send_keys("Lana")
            print("Input First Name")
            time.sleep(2)

            last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
            last_name.send_keys("Sokol")
            print("Input Last Name")
            time.sleep(2)

            zip_code = driver.find_element(By.XPATH, "//input[@id='postal-code']")
            zip_code.send_keys("1234")
            print("Input Zip code")
            time.sleep(2)

            button_continue = driver.find_element(By.XPATH, "//input[@id='continue']")
            button_continue.click()
            print("Click continue button")

            """"INFO Finish Product #4"""
            finish_product_4 = driver.find_element(By.XPATH, "//a[@id='item_5_title_link']")
            value_finish_product_4 = finish_product_4.text
            print(value_finish_product_4)
            assert number4 == value_finish_product_4
            print("INFO finish Product 4 GOOD")

            # проверка на соответствие названия товара на главной странице товару в корзине
            price_finish_product = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
            value_finish_price_product = price_finish_product.text
            print(value_finish_price_product)
            assert value_price_number4 == value_finish_price_product
            print("INFO Price finish Product 4 GOOD")

            summary_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[6]")
            value_summary_price = summary_price.text
            print(value_summary_price)

            item_total = "Item total: " + value_finish_price_product
            print(item_total)
            assert value_summary_price == item_total
            print("Total summary price Good")

            # Возврат на страницу каталога

            button_finish = driver.find_element(By.XPATH, "//button[@id='finish']")
            button_finish.click()
            print("Click Button Finish")

            button_back_home = driver.find_element(By.XPATH, "//button[@id ='back-to-products']")
            button_back_home.click()
            print("Click Button Back Home")

        elif products == 5:
            print(number5)

            """"INFO Product #5"""
            product_5 = driver.find_element(By.XPATH, "//a[@id='item_2_title_link']")
            number5 = product_5.text
            print(number5)

            price_product_5 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[5]/div[2]/div[2]/div")
            value_price_number5 = price_product_5.text
            print(value_price_number5)
            time.sleep(2)

            select_product_5 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']")
            select_product_5.click()
            print("Click select product 5")
            time.sleep(2)

            cart = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
            cart.click()
            print("Enter Cart")
            time.sleep(2)

            """INFO Cart Product #5"""
            cart_product_5 = driver.find_element(By.XPATH, "//a[@id='item_2_title_link']")
            value_cart_product_5 = cart_product_5.text
            print(value_cart_product_5)
            assert number5 == value_cart_product_5
            print("INFO Cart Product 5 GOOD")

            # проверка на соответствие названия товара на главной странице товару в корзине
            price_cart_product = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
            value_cart_price_product = price_cart_product.text
            print(value_cart_price_product)
            assert value_price_number5 == value_cart_price_product
            print("INFO Price Cart Product 5 GOOD")

            button_checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
            button_checkout.click()
            print("Click Checkout")
            time.sleep(2)

            """"Select User INFO"""
            first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
            first_name.send_keys("Lana")
            print("Input First Name")
            time.sleep(2)

            last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
            last_name.send_keys("Sokol")
            print("Input Last Name")
            time.sleep(2)

            zip_code = driver.find_element(By.XPATH, "//input[@id='postal-code']")
            zip_code.send_keys("1234")
            print("Input Zip code")
            time.sleep(2)

            button_continue = driver.find_element(By.XPATH, "//input[@id='continue']")
            button_continue.click()
            print("Click continue button")

            """"INFO Finish Product #5"""
            finish_product_5 = driver.find_element(By.XPATH, "//a[@id='item_2_title_link']")
            value_finish_product_5 = finish_product_5.text
            print(value_finish_product_5)
            assert number5 == value_finish_product_5
            print("INFO finish Product 5 GOOD")

            # проверка на соответствие названия товара на главной странице товару в корзине
            price_finish_product = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
            value_finish_price_product = price_finish_product.text
            print(value_finish_price_product)
            assert value_price_number5 == value_finish_price_product
            print("INFO Price finish Product 5 GOOD")

            summary_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[6]")
            value_summary_price = summary_price.text
            print(value_summary_price)

            item_total = "Item total: " + value_finish_price_product
            print(item_total)
            assert value_summary_price == item_total
            print("Total summary price Good")

            # Возврат на страницу каталога

            button_finish = driver.find_element(By.XPATH, "//button[@id='finish']")
            button_finish.click()
            print("Click Button Finish")

            button_back_home = driver.find_element(By.XPATH, "//button[@id ='back-to-products']")
            button_back_home.click()
            print("Click Button Back Home")

        elif products == 6:

            """"INFO Product #6"""
            product_6 = driver.find_element(By.XPATH, "//a[@id='item_3_title_link']")
            number6 = product_6.text
            print(number6)
            price_product_6 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[6]/div[2]/div[2]/div")
            value_price_number6 = price_product_6.text
            print(value_price_number6)
            time.sleep(2)

            select_product_6 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
            select_product_6.click()
            print("Click select product 6")
            time.sleep(2)

            cart = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
            cart.click()
            print("Enter Cart")
            time.sleep(2)

            """INFO Cart Product #6"""
            cart_product_6 = driver.find_element(By.XPATH, "//a[@id='item_3_title_link']")
            value_cart_product_6 = cart_product_6.text
            print(value_cart_product_6)
            assert number6 == value_cart_product_6
            print("INFO Cart Product 6 GOOD")

            # проверка на соответствие названия товара на главной странице товару в корзине
            price_cart_product = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
            value_cart_price_product = price_cart_product.text
            print(value_cart_price_product)
            assert value_price_number6 == value_cart_price_product
            print("INFO Price Cart Product 6 GOOD")

            button_checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
            button_checkout.click()
            print("Click Checkout")
            time.sleep(2)

            """"Select User INFO"""
            first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
            first_name.send_keys("Lana")
            print("Input First Name")
            time.sleep(2)

            last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
            last_name.send_keys("Sokol")
            print("Input Last Name")
            time.sleep(2)

            zip_code = driver.find_element(By.XPATH, "//input[@id='postal-code']")
            zip_code.send_keys("1234")
            print("Input Zip code")
            time.sleep(2)

            button_continue = driver.find_element(By.XPATH, "//input[@id='continue']")
            button_continue.click()
            print("Click continue button")

            """"INFO Finish Product #6"""
            finish_product_6 = driver.find_element(By.XPATH, "//a[@id='item_3_title_link']")
            value_finish_product_6 = finish_product_6.text
            print(value_finish_product_6)
            assert number6 == value_finish_product_6
            print("INFO finish Product 6 GOOD")

            # проверка на соответствие названия товара на главной странице товару в корзине
            price_finish_product = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
            value_finish_price_product = price_finish_product.text
            print(value_finish_price_product)
            assert value_price_number6 == value_finish_price_product
            print("INFO Price finish Product 6 GOOD")

            summary_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[6]")
            value_summary_price = summary_price.text
            print(value_summary_price)

            item_total = "Item total: " + value_finish_price_product
            print(item_total)
            assert value_summary_price == item_total
            print("Total summary price Good")

            # Возврат на страницу каталога

            button_finish = driver.find_element(By.XPATH, "//button[@id='finish']")
            button_finish.click()
            print("Click Button Finish")

            button_back_home = driver.find_element(By.XPATH, "//button[@id ='back-to-products']")
            button_back_home.click()
            print("Click Button Back Home")
            break
        else:
            raise ValueError
    except ValueError:
        print("Вы ввели не число или число не входит в указанный диапазон. Попробуйте снова: ")
