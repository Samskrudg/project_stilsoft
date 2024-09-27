from selenium.webdriver.common.by import By


class MainPageLocators:
    CARD_PRODUCT = (By.CLASS_NAME, "product")
    IMAGE_PRODUCT = (By.CLASS_NAME, "imgCont")
    SERVICE_LIFE = (By.XPATH, '//*[@id="tab-1"]/ul[4]/li[2]')
