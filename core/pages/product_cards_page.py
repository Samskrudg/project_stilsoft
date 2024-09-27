from core.locators import ProductCardsPageLocators

from .base_page import BasePage
from .product_page import ProductPage


class ProductCardsPage(BasePage):
    def get_products_urls(self) -> list[str]:
        web_elements = self.browser.find_elements(*ProductCardsPageLocators.CARD_LINKS)
        links = [element.get_attribute("href") for element in web_elements]

        return links

    def open_product_page(self, url: str) -> ProductPage:
        self.open(url)
        
        return ProductPage(self.browser)
    