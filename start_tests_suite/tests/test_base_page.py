import allure
from start_tests_suite.pages.base_page import base_page


@allure.epic('Base page')
@allure.story('Open base page')
@allure.title('Base page should be shown')
@allure.feature('Base page')
@allure.label('microservice', 'Base page')
@allure.label('owner', 'Alexander Osipkin')
@allure.tag('smoke', 'regress', 'web', 'critical')
@allure.severity('critical')
@allure.label('layer', 'web')
def test_base_page():
    with allure.step("Открываем главную страницу онлайн кинотеатра start.ru"):
        base_page.open_main_page()

    with allure.step("Проверяем кнопку Фильмы"):
        base_page.check_movies_button()

    with allure.step("Проверяем кнопку Сериалы"):
        base_page.check_series_button()

    with allure.step("Проверяем кнопку Мультфильмы"):
        base_page.check_animation_button()

    with allure.step("Проверяем кнопку Новинки"):
        base_page.check_new_button()

    with allure.step("Проверяем кнопку Журнал"):
        base_page.check_journal_button()

    with allure.step("Проверяем кнопку ТВ"):
        base_page.check_tv_button()
