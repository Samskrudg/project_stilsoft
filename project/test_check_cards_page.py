from pages.check_cards_page import CheckCardsPage


def test_go_to_product_page(browser):
    link = "https://stilsoft.ru/products/kitsoz-synerget"
    page = CheckCardsPage(browser, link)
    page.open()
    page.go_to_product_page()
    page.take_current_url()
    page.check_image_presence()
    page.check_assigned_service_life()
    page.check_requirements()
