from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")

    def browse_cat(self):
        INPUT_LOCATOR = (By.XPATH, "//input[@id='searchInput']")
        SEARCH_BTN_LOCATOR = (By.XPATH, "//input[@id='searchButton']")

        inputf = self.driver.find_element(*INPUT_LOCATOR)
        inputf.send_keys("Кот")
        sbm_btn = self.driver.find_element(*SEARCH_BTN_LOCATOR)
        sbm_btn.click()