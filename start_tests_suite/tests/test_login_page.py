import allure
from start_tests_suite.pages.login_page import login_page


@allure.epic('Login page')
@allure.story('Login')
@allure.title('Login')
@allure.feature('PLogin page')
@allure.label('microservice', 'user login')
@allure.label('owner', 'Alexander Osipkin')
@allure.tag('regress', 'web')
@allure.severity('critical')
@allure.label('layer', 'web')
def test_login_page():
    with allure.step("Открываем главную страницу онлайн кинотеатра start.ru"):
        login_page.open_maim_page()

    with allure.step("Нажимаем на аватар неавторизованного пользователя"):
        login_page.click_avatar_button()

    with allure.step("Нажимаем на кнопку логина"):
        login_page.click_login_button()

    with allure.step("Вводим емеил пользователя"):
        login_page.enter_email()

    with allure.step("Вводим пароль пользователя"):
        login_page.enter_password()

    with allure.step("Нажимаем на кнопку авторизации"):
        login_page.press_login_button()
