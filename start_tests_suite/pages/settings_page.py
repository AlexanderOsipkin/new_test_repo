import os
from selene import browser, be
from dotenv import load_dotenv


class SettingsPage:

    # авторизируем пользователя в приложении

    def load_env(self):
        load_dotenv()
        return self

    login = os.getenv('USER_LOGIN')
    password = os.getenv('USER_PASSWORD')

    def open_maim_page(self):
        browser.open('/')
        return self

    def click_avatar_button(self):
        browser.element('.HeaderMenu_header-menu__avatar-adult__kpDMs').click()
        return self

    def click_login_button(self):
        browser.element(
            '.HeaderMenuAuthorization_menu-authorization__block__qgrem > span'
        ).click()
        return self

    def enter_email(self):
        browser.element('[id="signField"]').should(be.blank).type('{USER_LOGIN}')
        return self

    def enter_password(self):
        browser.element('[id="signPassword"]').should(be.blank).type('{USER_PASSWORD}')
        return self

    def press_login_button(self):
        browser.element('[data-testid="signin_button_text"]').click()
        return self

    # заходим в настройки аккаунта пользователя

    def press_settings_button(self):
