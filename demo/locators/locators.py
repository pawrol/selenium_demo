
class BillingAddress:

    register_email = find_element_by_id('reg_email')
    register_pass = find_element_by_id('reg_password')
    register_button = find_element_by_name("register")
    adresses_link = find_element_by_link_text("Addresses")
    edit_link = find_element_by_link_text("Edit")
    billing_first_name = find_element_by_id("billing_first_name")
    billing_last_name = find_element_by_id("billing_last_name")
    billing_company_name = find_element_by_id("billing_company")
    billing_country = find_element_by_id("billing_country")
    billing_addres_1 = find_element_by_id("billing_address_1")
    billing_addres_2 = find_element_by_id("billing_address_2")
    billing_postcode = find_element_by_id("billing_postcode")
    billing_city = find_element_by_id("billing_city")
    billing_phone = find_element_by_id("billing_phone")
    save_data_button = find_element_by_class_name("button")
    assert_text = driver.find_element_by_xpath("//div[@class = 'woocommerce-message']")


class MyAccountPage:

    username = find_element_by_id('username')
    password = find_element_by_id('password')
    login_button = find_element_by_name("login")
    register_email = find_element_by_id('reg_email')
    register_password = driver.find_element_by_id('reg_password')
    register_button = find_element_by_name("register")
    logout_link = find_element_by_link_text("Logout")
    assert_text_error = find_element_by_xpath("//ul[@class = 'woocommerce-error']//li")