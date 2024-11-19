import os
from selene import browser, be
from dotenv import load_dotenv


class LoginPage:

    def open_maim_page(self):
        browser.open('/')
        return self

    def click_avatar_button(self):
        browser.element('.HeaderMenu_header-menu__login-button__4PeyG').click()
        return self

    def click_login_button(self):
        browser.element(
            '.HeaderMenuAuthorization_menu-authorization__block__qgrem > span'
        ).click()
        return self

    def enter_email(self):
        load_dotenv()
        login = os.getenv('USER_LOGIN')
        browser.element('[id="login"]').should(be.blank).type(login).press_enter()
        return self

    def enter_password(self):
        load_dotenv()
        password = os.getenv('USER_PASSWORD')
        browser.element('[id="password"]').should(be.blank).type(password)
        return self

    def press_login_button(self):
        browser.element('[testid="signin_button"]').click()
        return self


login_page = LoginPage()
