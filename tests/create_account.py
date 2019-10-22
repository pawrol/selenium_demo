import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest

from pages.my_account_page import MyAccountPage


@pytest.mark.usefixtures("setup")
class TestCreateAccount:

    def test_account_register_failed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_webpage()
        my_account_page.create_account("kokosz@lp.eu", "kokosz@lp.eu")
        error_login = "An account is already registered with your email address. Please log in."
        assert error_login in my_account_page.error_msg()

    def test_account_register_passed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_webpage()
        random_mail = "kokosz" + str(random.randint(1, 10000)) + "@lp.eu"
        my_account_page.create_account(random_mail, random_mail)
        assert my_account_page.logout_displayed()
