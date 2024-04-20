from selene import browser, have, be


class PromotionPage:
    def open_main_page(self):
        browser.open("/")
        return self

    def click_to_the_promotion_button(self):
        browser.element('[data-testid="try_free_button_text"]').click()
        return self

    def check_promotion_page(self):
        browser.element(
            '#CybotCookiebotDialogBodyButtonsWrapper #CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll'
        ).click()
        browser.element('.Feature_heading__MFqx2 .Feature_title__6aQjy').should(
            have.text("СОЗДАЁМ И ПОКАЗЫВАЕМ ШЕДЕВРЫ КАЖДУЮ НЕДЕЛЮ")
        )
        return self

    def click_to_the_try_button(self):
        browser.element('.SubscriptionButton_button__c9yq2 .Button_text__CEKtw').click()
        browser.element('[data-testid="payment_button_text"]').should(
            have.text("Зарегистрироваться")
        )
        return self


promotion_banner = PromotionPage()
