import pytest
from conftest import driver_setup
from pages.login import Login

@pytest.fixture
def login_page(driver_setup):
    driver_setup.get("https://habr.com/")
    login_obj = Login(driver_setup)
    login_obj.navigate_to_login_page()
    return login_obj

# @pytest.mark.loginsuccess
# def test_login(driver_setup, login_page):
#     login_page.login("standard_user", "secret_sauce")
#     assert True #TODO

# @pytest.mark.errormsg
# @pytest.mark.parametrize("email,password,error",
#     [("non_existing_email", "wrongpassword", "Error: Email and password do not match any user in this service")])
# def test_login_error(driver_setup, login_page, email, password, error):
#     login_page.login(email, password)
#     assert True #TODO
