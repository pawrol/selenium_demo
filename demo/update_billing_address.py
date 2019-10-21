import random

from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


def test_update_addres():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("http://seleniumdemo.com/")
    driver.find_element_by_xpath("//li[@id = 'menu-item-22']//a").click()
    random_mail = "kokosz" + str(random.randint(1, 10000)) + "@lp.eu"
    driver.find_element_by_id('reg_email').send_keys(random_mail)
    driver.find_element_by_id('reg_password').send_keys("kokosz@lp.eu")
    driver.find_element_by_name("register").click()
    driver.find_element_by_link_text("Addresses").click()
    driver.find_element_by_link_text("Edit").click()
    driver.find_element_by_id("billing_first_name").send_keys("Jan")
    driver.find_element_by_id("billing_last_name").send_keys("Nowak")
    driver.find_element_by_id("billing_company").send_keys("Jan_company")
    Select(driver.find_element_by_id("billing_country")).select_by_value("PL")
    driver.find_element_by_id("billing_address_1").send_keys("ul. Jasna")
    driver.find_element_by_id("billing_address_2").send_keys("34")
    driver.find_element_by_id("billing_postcode").send_keys("11-222")
    driver.find_element_by_id("billing_city").send_keys("Kraków")
    driver.find_element_by_id("billing_phone").send_keys("111-222-333")
   # if driver.find_element_by_id("billing_email").text == random_mail:
      #  driver.find_element_by_id("billing_email").send_keys(random_mail)
    driver.find_element_by_class_name("button").click()
    address_chanded_text = "Address changed successfully."
    print(random_mail)
    assert address_chanded_text in driver.find_element_by_class_name("woocommerce-message").text

test_update_addres()