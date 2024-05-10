import allure
from start_tests_suite.pages.promotion_page import promotion_banner


@allure.epic('Promo page')
@allure.story('Use promo button')
@allure.title('Promo button will be shown')
@allure.feature('Promo page')
@allure.label('microservice', 'promo page')
@allure.label('owner', 'Alexander Osipkin')
@allure.tag('regress', 'web')
@allure.severity('major')
@allure.label('layer', 'web')
def test_promotion_banner():
    with allure.step("Открываем главную страницу онлайн кинотеатра start.ru"):
        promotion_banner.open_main_page()

    with allure.step("Открываем страницу промоакции"):
        promotion_banner.check_promotion_page()

    with allure.step("Нажимаем на кнопу Попробовать"):
        promotion_banner.click_to_the_try_button()
