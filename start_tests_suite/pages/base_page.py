from selene import browser, have


class BasePage:

    def open_main_page(self):
        browser.open("/")
        return self

    def check_movies_button(self):
        browser.element('[data-testid="movies_button"]').click()
        browser.element('.BreadCrumbs_breadcrumbs_point-name__6F2fE').should(
            have.text("Фильмы")
        )
        return self

    def check_series_button(self):
        browser.element('[data-testid="series_button"]').click()
        browser.element('.BreadCrumbs_breadcrumbs_point-name__6F2fE').should(
            have.text("Сериалы")
        )
        return self

    def check_animation_button(self):
        browser.element('[data-testid="animation_button"]').click()
        browser.element('.BreadCrumbs_breadcrumbs_point-name__6F2fE').should(
            have.text("Мультфильмы")
        )
        return self

    def check_new_button(self):
        browser.element('[data-testid="new_button"]').click()
        browser.element('.BreadCrumbs_breadcrumbs_point-name__6F2fE').should(
            have.text("Новинки")
        )
        return self

    def check_journal_button(self):
        browser.element('[data-testid="header_journal_button"]').click()
        browser.element('.BreadCrumbs_breadcrumbs_point-name__6F2fE').should(
            have.text("Журнал")
        )
        return self

    def check_tv_button(self):
        browser.element('[data-testid="tv_button"]').click()
        browser.element('.BreadCrumbs_breadcrumbs_point-name__6F2fE').should(
            have.text("ТВ")
        )
        return self


base_page = BasePage()
