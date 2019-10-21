import random

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def test_account_register_failed():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("http://seleniumdemo.com/")
    driver.find_element_by_xpath("//li[@id = 'menu-item-22']//a").click()
    driver.find_element_by_id('reg_email').send_keys("kokosz@lp.eu")
    driver.find_element_by_id('reg_password').send_keys("kokosz@lp.eu")
    driver.find_element_by_name("register").click()
    error_login = "An account is already registered with your email address. Please log in."
    assert error_login in driver.find_element_by_xpath("//ul[@class = 'woocommerce-error']//li").text

def test_account_register_passed():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("http://seleniumdemo.com/")
    driver.find_element_by_xpath("//li[@id = 'menu-item-22']//a").click()
    random_mail = "kokosz" + str(random.randint(1, 10000)) + "@lp.eu"
    driver.find_element_by_id('reg_email').send_keys(random_mail)
    driver.find_element_by_id('reg_password').send_keys("kokosz@lp.eu")
    driver.find_element_by_name("register").click()
    assert driver.find_element_by_link_text("Logout").is_displayed()

test_account_register_failed()