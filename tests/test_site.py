from pages.homepage import HomePage
from pages.abstractpage import AbstractPage



def test_open_wiki(driver):
    homepage = HomePage(driver)
    abstractpage = AbstractPage(driver)
    homepage.open()
    homepage.browse_cat()
    abstractpage.check_title("Кошка")

