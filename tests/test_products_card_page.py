def test_product_cards(base_page, clear_results_file):
    cards_page = base_page.go_to_product_cards_page()

    product_urls = cards_page.get_products_urls()

    for url in product_urls:
        product_page = cards_page.open_product_page(url=url)
        product_page.check_product()
