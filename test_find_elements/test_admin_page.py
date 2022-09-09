from page_objects import LoginAdminPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_page_check_elements(browser):
    browser.get(browser.url + "admin")
    wait = WebDriverWait(browser, 2, poll_frequency=1)
    browser.find_element(*LoginAdminPage.USERNAME_INPUT)
    browser.find_element(*LoginAdminPage.PASSWORD_INPUT)
    wait.until(EC.visibility_of_element_located(LoginAdminPage.SUBMIT_BUTTON))
    browser.find_element(*LoginAdminPage.SUBMIT_BUTTON)
    browser.find_element(*LoginAdminPage.FORGOTTEN_PASSWORD)
    wait.until(EC.visibility_of_element_located(LoginAdminPage.OPENCART_LINK))


def test_admin_page_input(browser):
    browser.get(browser.url + "admin")
    wait = WebDriverWait(browser, 1, poll_frequency=1)
    wait.until(EC.visibility_of_element_located(LoginAdminPage.USERNAME_INPUT)).send_keys(*LoginAdminPage.USERNAME)
    wait.until(EC.visibility_of_element_located(LoginAdminPage.PASSWORD_INPUT)).send_keys(*LoginAdminPage.PASSWORD)
    wait.until(EC.visibility_of_element_located(LoginAdminPage.SUBMIT_BUTTON)).click()
    tag_one_element = browser.find_element(*LoginAdminPage.ADMIN_PANEL_ONE_ELEMENT)
    tag_two_element = browser.find_element(*LoginAdminPage.ADMIN_PANEL_TWO_ELEMENT)
    tag_three_element = browser.find_element(*LoginAdminPage.ADMIN_PANEL_THREE_ELEMENT)
    tag_four_element = browser.find_element(*LoginAdminPage.ADMIN_PANEL_FOUR_ELEMENT)
    tag_five_element = browser.find_element(*LoginAdminPage.ADMIN_PANEL_FIVE_ELEMENT)
    assert tag_one_element.text == "TOTAL ORDERS\n0%"
    assert tag_two_element.text == "TOTAL SALES\n0%"
    assert tag_three_element.text == "TOTAL CUSTOMERS\n0%"
    assert tag_four_element.text == "World Map"
    assert tag_five_element.text == "Reports"
