from selenium.webdriver.ie.webdriver import WebDriver

from core.links import Link


class BasePage:
    def __init__(self, browser: WebDriver, timeout: int = 10):
        self.browser = browser
        self.browser.implicitly_wait(timeout)

        self.base_url = "https://stilsoft.ru"

    def open(self, url: str):
        if "http" in url:
            self.browser.get(url)
        else:
            self.browser.get(self.base_url + url)

    def go_to_product_cards_page(self):
        from .product_cards_page import ProductCardsPage

        self.open(Link.PRODUCTS_KITSOZ_SYNERGET)

        return ProductCardsPage(self.browser)
