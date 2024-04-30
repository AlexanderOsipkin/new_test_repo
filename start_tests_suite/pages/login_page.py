from selene import browser, have, be


class LoginPage:

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
        browser.element('[id="signField"]').should(be.blank).type(
            'qagurutestuser@yandex.ru'
        )
        return self

    def enter_password(self):
        browser.element('[id="signPassword"]').should(be.blank).type('qagurutestuser1')
        return self

    def press_login_button(self):
        browser.element('[data-testid="signin_button_text"]').click()
        return self


login_page = LoginPage()
