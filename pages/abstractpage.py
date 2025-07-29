from selenium.webdriver.common.by import By


class AbstractPage:

    def __init__(self, driver):
        self.driver = driver


    def check_title(self, title):
        TITLE_LOCATOR = (By.XPATH, "//span[@class='mw-page-title-main']")
        title_text = self.driver.find_element(*TITLE_LOCATOR)
        assert title_text.text == title