from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def test_log_in():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    driver.get("http://seleniumdemo.com/")
    driver.find_element_by_xpath("//li[@id = 'menu-item-22']//a").click()
    driver.find_element_by_id('username').send_keys("kokosz@lp.eu")
    driver.find_element_by_id('password').send_keys("123")
    driver.find_element_by_name("login").click()


