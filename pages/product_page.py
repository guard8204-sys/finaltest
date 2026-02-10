from .base_page import BasePage
from .locators import ProductPageLocators 

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()

    def should_be_correct_product_name_in_basket_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        product_name_alert = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_SUCCESS_MESSAGE).text
        assert product_name == product_name_alert, f"Expected {product_name}, got {product_name_alert}"

    def should_be_correct_basket_total_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_PRICE).text
        assert product_price == basket_price, f"Expected {product_price}, got {basket_price}"

    def should_not_be_success_message(self):
        """Нет сообщения об успехе изначально"""
        return self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)

    def should_be_success_message_disappeared(self):
        """Сообщение об успехе исчезло"""
        return self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)
