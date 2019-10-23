from locators import locators
from selenium.webdriver.support.select import Select

class BillingAdressPage:

    def __init__(self, driver):
        self.driver = driver
        self.username = locators.BillingAddress.username
        self.password = locators.BillingAddress.pass_username
        self.loginbutton = locators.BillingAddress.login_button
        self.adress_link = locators.BillingAddress.adresses_link
        self.edit_link = locators.BillingAddress.edit_link
        self.first_name = locators.BillingAddress.billing_first_name
        self.last_name = locators.BillingAddress.billing_last_name
        self.company_name = locators.BillingAddress.billing_company_name
        self.country = locators.BillingAddress.billing_country
        self.addres_1 = locators.BillingAddress.billing_addres_1
        self.addres_2 = locators.BillingAddress.billing_addres_2
        self.postcode = locators.BillingAddress.billing_postcode
        self.city = locators.BillingAddress.billing_city
        self.phone = locators.BillingAddress.billing_phone
        self.save_data = locators.BillingAddress.save_data_button
        self.assert_text = locators.BillingAddress.assert_text

    def open_webpage(self):
        self.driver.get("http://seleniumdemo.com/?page_id=7")

    def login(self, login, password):
        self.driver.find_element_by_id(self.username).send_keys(login)
        self.driver.find_element_by_id(self.password).send_keys(password)
        self.driver.find_element_by_name(self.loginbutton).click()

    def open_editlink(self):
        self.driver.find_element_by_link_text(self.adress_link).click()
        self.driver.find_element_by_class_name(self.edit_link).click()

    def billing_addres(self, name, name2, company, addres1, addres2, postcode, city, phone):
        self.driver.find_element_by_id(self.first_name).send_keys(name)
        self.driver.find_element_by_id(self.last_name).send_keys(name2)
        self.driver.find_element_by_id(self.addres_1).send_keys(addres1)
        self.driver.find_element_by_id(self.addres_2).send_keys(addres2)
        self.driver.find_element_by_id(self.postcode).send_keys(postcode)
        self.driver.find_element_by_id(self.city).send_keys(city)
        self.driver.find_element_by_id(self.phone).send_keys(phone)
        self.driver.find_element_by_id(self.company_name).send_keys(company)
        self.driver.find_element_by_class_name(self.save_data).click()

    def billing_addres_country(self, count):
        select = Select(self.driver.find_element_by_id(self.country))
        select.select_by_visible_text(count)

    def error_msg(self):
       return self.driver.find_element_by_xpath(self.assert_text).text
