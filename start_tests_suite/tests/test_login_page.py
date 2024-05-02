import allure
from start_tests_suite.pages.login_page import login_page


@allure.epic('Login page')
@allure.story('Login')
@allure.title('Login')
@allure.feature('PLogin page')
@allure.label('microservice', 'login page')
@allure.label('owner', 'Alexander Osipkin')
@allure.tag('smoke', 'regress', 'web')
@allure.severity('critical')
@allure.label('layer', 'web')
def test_login_page():
    login_page.open_maim_page()
    login_page.click_avatar_button()
    login_page.click_login_button()
    login_page.enter_email()
    login_page.enter_password()
    login_page.press_login_button()
