from page_objects import StartPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_start_page_check_elements(browser):
    browser.get(browser.url)
    wait = WebDriverWait(browser, 2, poll_frequency=1)
    phone = wait.until(EC.visibility_of_element_located(StartPage.PHONE_NUMBER))
    add_cart = wait.until(EC.visibility_of_element_located(StartPage.ADD_TO_CART))
    wait.until(EC.visibility_of_element_located(StartPage.FEATURED))
    wait.until(EC.visibility_of_element_located(StartPage.INFORMATION))
    wait.until(EC.visibility_of_element_located(StartPage.LINK_MENU))
    assert phone.text == "123456789"
    assert add_cart.text == "ADD TO CART"

