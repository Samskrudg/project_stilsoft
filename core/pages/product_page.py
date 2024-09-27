import re

from selenium.common.exceptions import NoSuchElementException

from core.locators import ProductPageLocators

from .base_page import BasePage


class ProductPage(BasePage):
    def check_product(self):
        try:
            self.check_image_presence()
            self.check_assigned_service_life()
        except AssertionError as e:
            print(f"Произошла ошибка при проверке карточки товара. Карточка - {self.browser.current_url}, ошибка - {e}")
            self._write_product_file()

    def check_image_presence(self):
        check_picture = self.browser.find_element(*ProductPageLocators.IMAGE_PRODUCT).is_displayed()
        assert check_picture is True, 'Нет изображения товара на странице'

    def check_assigned_service_life(self):
        try:
            service_life_sentence = self.browser.find_element(*ProductPageLocators.SERVICE_LIFE).text
        except NoSuchElementException:
            print(f"На странице '{self.browser.current_url}' не найдена информация про назначенный срок службы")
            self._write_product_file()
            return
        service_life_digit = re.search(r"\d+", service_life_sentence).group(0)
        assert int(service_life_digit) >= 10, 'Назначенный срок службы меньше 10 лет'
    
    def _write_product_file(self):
        with open('results.txt', "a") as f:
            f.write(self.browser.current_url + '\n')
    