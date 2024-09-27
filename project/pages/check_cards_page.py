from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import


class CheckCardsPage(BasePage):
    def go_to_product_page(self):
        product_link = self.browser.find_elements(*MainPageLocators.CARD_PRODUCT)
        product_link.click()

    def back_browser(self):
        return_catalog = self.browser
        return_catalog.back()

    def take_current_url(self):
        self.current_url = self.browser.current_url

    def check_image_presence(self):
        check_picture = self.browser.find_element(*MainPageLocators.IMAGE_PRODUCT).is_displayed()
        assert check_picture == True, 'Нет изображение товара на странице'

    def check_assigned_service_life(self):
        check_service_life = self.browser.find_element(*MainPageLocators.SERVICE_LIFE).text
        assert int((check_service_life.split()[4])) >= 10, 'Назначенный срок службы меньше необходимого'

    def write_product_file(self):
        with open(r'result.txt', "w") as file:
            file.write(self.browser.current_url + '\n')

    def check_requirements(self):
        self.take_current_url()
        count = 0
        web_elements = self.go_to_product_page()[count]
        for element in range(len(web_elements)):
             web_elements[count].click()
             self.back_browser()
             web_elements = WebDriverWait(browser, 10).until(
                 EC.presence_of_all_elements_located((*MainPageLocators.CARD_PRODUCT)))
             count += 1
            try:
                self.check_image_presence()
                self.check_assigned_service_life()
            except AssertionError as e:
                print(f"Проверка не пройдена: {e}")
                self.write_product_file()

