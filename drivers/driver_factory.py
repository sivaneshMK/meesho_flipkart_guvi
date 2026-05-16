from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.firefox.options import Options as firefox_options

class DriverFactory:

    __driver = None

    @classmethod
    def get_driver(cls, browser):
        if cls.__driver is None:
            if browser.lower() == "chrome":
                options = chrome_options()
                options.add_argument("--start-maximized")
                cls.__driver = webdriver.Chrome(options)
            elif browser.lower() =="firefox":
                options = firefox_options()
                cls.__driver =webdriver.Firefox(options)
        return cls.__driver

    @classmethod
    def quit_driver(cls):
        if cls.__driver:
            cls.__driver.quit()
            cls.__driver=None