from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def go_to_product_page(self):
        product_link = self.browser.find_element(*MainPageLocators.CARD_PRODUCT)
        product_link.click()

    def take_current_url(self):
        self.current_url = self.browser.current_url

    def check_image_presence(self):
        check_picture = self.browser.find_element(*MainPageLocators.IMAGE_PRODUCT).is_displayed()
        assert check_picture == True, 'Картинки там нет'

    def check_assigned_service_life(self):
        check_service_life = self.browser.find_element(*MainPageLocators.SERVICE_LIFE)
        assert check_service_life.text == "Назначенный срок службы – 8 лет.", 'Назначенный срок службы не подходит'

    def write_product_file(self):
        with open(r'C:\Users\dan4ik_samara\Pycharm\Stilsoft\result.txt', "w") as file:
            file.write(self.browser.current_url + '\n')

    def  check_requirements(self):
        self.take_current_url()
        try:
            self.check_image_presence()
            self.check_assigned_service_life()
        except AssertionError as e:
            print(f"Проверка не пройдена: {e}")
            self.write_product_file()