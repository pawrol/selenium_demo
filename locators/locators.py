
class BillingAddress:
    username = 'username'
    pass_username = 'password'
    login_button = "login"
    adresses_link = "Addresses"
    edit_link = "edit"
    billing_first_name = "billing_first_name"
    billing_last_name = "billing_last_name"
    billing_company_name = "billing_company"
    billing_country = "billing_country"
    billing_addres_1 = "billing_address_1"
    billing_addres_2 = "billing_address_2"
    billing_postcode = "billing_postcode"
    billing_city = "billing_city"
    billing_phone = "billing_phone"
    save_data_button = "button"
    assert_text = "//div[@class = 'woocommerce-message']"


class MyAccountPage:

    username = 'username'
    password = 'password'
    login_button = "login"
    register_email = 'reg_email'
    register_password = 'reg_password'
    register_button = "register"
    logout_link = "Logout"
    assert_text_error = "//ul[@class = 'woocommerce-error']//li"