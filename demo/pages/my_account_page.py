from locators import locators


class MyAccountPage

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

    def login(self, username, password):
        self.driver.username_input.send_keys(username)
        self.driver.password_input.send_keys(password)