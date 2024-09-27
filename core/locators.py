from selenium.webdriver.common.by import By


class ProductCardsPageLocators:
    CARD_LINKS = (By.XPATH, '//div[@class="product"]/a[1]')


class ProductPageLocators:
    IMAGE_PRODUCT = (By.XPATH, '//img[@class="imgCont"]')
    SERVICE_LIFE = (By.XPATH, '//div[@id="tab-1"]//li[contains(text(), "Назначенный срок службы")]')
