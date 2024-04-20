import allure
from start_tests_suite.pages.promotion_page import promotion_banner


def test_promotion_banner():
    promotion_banner.open_main_page()
    promotion_banner.check_promotion_page()
    promotion_banner.click_to_the_try_button()
