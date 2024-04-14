from selene import browser, have, be


class BasePage:

    def open_main_page(self):
        browser.open("/")
        return self

    def check_movies_button(self):
        browser.element('[data-testid="movies_button"]').click()
        browser.element('.BreadCrumbs_breadcrumbs_point-name__6F2fE').should(
            have.texts('Фильмы')
        )
        return self

    def check_series_button(self):
        browser.element('[data-testid="series_button"]').click()
        browser.element('Catalog_catalog__Gjv4a').should(
            have.texts('Сериалы -  смотреть онлайн')
        )
        return self

    def check_animation_button(self):
        browser.element('[data-testid="animation_button"]').click()
        browser.element('.Catalog_catalog__Gjv4a').should(
            have.texts('Мультфильмы -  смотреть онлайн')
        )
        return self

    def check_new_button(self):
        browser.element('[data-testid="new_button"]').click()
        browser.element('.Genres_new_body__wWFFU').should(
            have.texts('Новинки фильмов, мультфильмов и сериалов смотреть онлайн ')
        )
        return self

    def check_journal_button(self):
        browser.element('[data-testid="header_journal_button"]').click()
        browser.element('.BreadCrumbs_breadcrumbs_point-name__6F2fE').should(
            have.texts('Журнал')
        )
        return self

    def check_tv_button(self):
        browser.open('[data-testid="tv_button"]').click()
        browser.element('[data-testid="hover_play_off"]').should(
            have.texts('ТВ Каналы Онлайн и Программа Передач')
        )
        return self


base_page = BasePage()
