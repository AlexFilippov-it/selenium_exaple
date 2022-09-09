from page_objects import ProductPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_start_page_check_elements(browser):
    browser.get(browser.url + "desktops/canon-eos-5d")
    wait = WebDriverWait(browser, 1, poll_frequency=1)
    wait.until(EC.visibility_of_element_located(ProductPage.TITLE_PRODUCT))
    wait.until(EC.visibility_of_element_located(ProductPage.PRICE_PRODUCT))
    available = wait.until(EC.visibility_of_element_located(ProductPage.AVAILABLE_OPTIONS))
    brand_name = wait.until(EC.visibility_of_element_located(ProductPage.BRAND))
    wait.until(EC.visibility_of_element_located(ProductPage.OLD_PRICE))
    assert available.text == "Available Options"
    assert brand_name.text == "Brand: Canon"
