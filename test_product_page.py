import pytest
import time
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage

# product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#
# @pytest.mark.parametrize('link', [
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#     pytest.param(
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#         marks=pytest.mark.xfail
#     ),  # ← Баг здесь!
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
# ])

# def test_guest_can_add_product_to_basket(browser, link):
#     page = ProductPage(browser, link)
#     page.open()
#
#     page.add_product_to_basket()
#     page.should_be_correct_product_name_in_basket_message()
#     page.should_be_correct_basket_total_price()

# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7"
# @pytest.mark.xfail
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_product_to_basket()
#     page.should_not_be_success_message()
#
# def test_guest_cant_see_success_message(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_not_be_success_message()
#
# @pytest.mark.xfail
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_product_to_basket()
#     page.should_be_success_message_disappeared()

# link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#
# def test_guest_should_see_login_link_on_product_page(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()
#
#
# def test_guest_can_go_to_login_page_from_product_page(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_to_login_page()
#     login_page = LoginPage(browser, browser.current_url)
#     login_page.should_be_login_page()
#
# def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_to_basket_page()
#     basket_page = BasketPage(browser, browser.current_url)
#     basket_page.should_be_basket_empty()
#     basket_page.should_not_be_product_in_basket()

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear"
login_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(autouse=True)
    def setup_method(self, browser):
        self.browser = browser
        email = str(time.time()) + "@fakemail.org"
        password = "testpass123"

        self.login_page = LoginPage(browser, login_link)
        self.login_page.open()
        self.login_page.register_new_user(email, password)

        self.product_page = ProductPage(browser, link)
        self.product_page.open()
        self.product_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self):
        self.product_page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self):
        self.product_page.add_product_to_basket()
        self.product_page.should_be_correct_product_name_in_basket_message()
        self.product_page.should_be_correct_basket_total_price()
