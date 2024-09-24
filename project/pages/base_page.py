

class BasePage:
    def __init__(self, browser: object, url: object, timeout: object = 10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)