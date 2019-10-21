from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def test_log_in_passed():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("http://seleniumdemo.com/")
    driver.find_element_by_xpath("//li[@id = 'menu-item-22']//a").click()
    driver.find_element_by_id('username').send_keys("kokosz@lp.eu")
    driver.find_element_by_id('password').send_keys("kokosz@lp.eu")
    driver.find_element_by_name("login").click()
    assert driver.find_element_by_link_text("Logout").is_displayed()

def test_log_in_failed():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("http://seleniumdemo.com/")
    driver.find_element_by_xpath("//li[@id = 'menu-item-22']//a").click()
    driver.find_element_by_id('username').send_keys("kokosz@lp.eu")
    driver.find_element_by_id('password').send_keys("123123")
    driver.find_element_by_name("login").click()
    assert  "ERROR: Incorrect username or password." in driver.find_element_by_xpath("//ul[@class = 'woocommerce-error']//li").text

