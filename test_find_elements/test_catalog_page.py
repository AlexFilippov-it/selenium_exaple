from page_objects import CatalogPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_start_page_check_elements(browser):
    browser.get(browser.url + "desktops")
    wait = WebDriverWait(browser, 1, poll_frequency=1)
    wait.until(EC.visibility_of_element_located(CatalogPage.REFINE_SEARCH))
    wait.until(EC.visibility_of_element_located(CatalogPage.ADD_TO_CART_CATALOG))
    wait.until(EC.visibility_of_element_located(CatalogPage.SHOW_RESULT_ON_PAGE))
    menu = wait.until(EC.visibility_of_element_located(CatalogPage.MENU_CATEGORY))
    menu_upper = wait.until(EC.visibility_of_element_located(CatalogPage.MENU_CATEGORY_UPPER))
    assert menu.text == "Laptops & Notebooks (5)"
    assert menu_upper.text == "MP3 Players"
