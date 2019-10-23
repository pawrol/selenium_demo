from locators import locators


class MyAccountPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_input = locators.MyAccountPage.username
        self.password_input = locators.MyAccountPage.password
        self.login_button = locators.MyAccountPage.login_button
        self.reg_email_input = locators.MyAccountPage.register_email
        self.reg_password_input = locators.MyAccountPage.register_password
        self.reg_button = locators.MyAccountPage.register_button
        self.log_out_link = locators.MyAccountPage.logout_link
        self.assert_text = locators.MyAccountPage.assert_text_error

    def open_webpage(self):
        self.driver.get("http://seleniumdemo.com/?page_id=7")

    def login(self, username, password):
        self.driver.find_element_by_id(self.username_input).send_keys(username)
        self.driver.find_element_by_id(self.password_input).send_keys(password)
        self.driver.find_element_by_name(self.login_button).click()

    def create_account(self, email, password):
        self.driver.find_element_by_id(self.reg_email_input).send_keys(email)
        self.driver.find_element_by_id(self.reg_password_input).send_keys(password)
        self.driver.find_element_by_name(self.reg_button).click()

    def logout_displayed(self):
        return self.driver.find_element_by_link_text(self.log_out_link).is_displayed()

    def error_msg(self):
       return self.driver.find_element_by_xpath(self.assert_text).text