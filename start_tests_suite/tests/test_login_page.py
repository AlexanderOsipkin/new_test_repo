import allure
from start_tests_suite.pages.login_page import login_page


def test_login_page():
    login_page.open_maim_page()
    login_page.click_avatar_button()
    login_page.click_login_button()
    login_page.enter_email()
    login_page.enter_password()
    login_page.press_login_button()
