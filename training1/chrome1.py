import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys


options = Options()
#options.page_load_strategy="eager"

options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)
action = ActionChains(driver)

SEARCH_INPUT = (By.XPATH, "//input[@id='searchInput']")
SEARCH_BTN = (By.XPATH, "//button[@type='submit']")
MAL_VODOSVINCA = (By.XPATH, "//a[@title='Малая водосвинка']")
LANG_SELECT_LOCATOR = (By.XPATH, "//select[@id='searchLanguage']")
IMG_LOCATOR = (By.XPATH, "(//img)[7]")

driver.get("https://www.wikipedia.org/")
time.sleep(2)

inp_feild = driver.find_element(*SEARCH_INPUT)
inp_feild.send_keys("Капибара")

driver.find_element(*SEARCH_BTN).click()
time.sleep(2)

print(driver.title)

driver.find_element(*MAL_VODOSVINCA).click()
time.sleep(2)

driver.back()
driver.back()
inp_feild.clear()
time.sleep(2)


lang_select = Select(driver.find_element(*LANG_SELECT_LOCATOR))
lang_select.select_by_value("en")

time.sleep(2)
inp_feild.send_keys("Cat" + Keys.ENTER)
time.sleep(2)

driver.find_element(*IMG_LOCATOR).click()
time.sleep(2)
driver.save_screenshot("screen.png")
