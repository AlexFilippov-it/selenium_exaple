from page_objects import PageRegistration
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_start_page_check_elements(browser):
    browser.get(browser.url + "index.php?route=account/register")
    wait = WebDriverWait(browser, 1, poll_frequency=1)
    wait.until(EC.visibility_of_element_located(PageRegistration.FIRST_NAME))
    wait.until(EC.visibility_of_element_located(PageRegistration.LAST_NAME))
    pass_word = wait.until(EC.visibility_of_element_located(PageRegistration.PASSWORD))
    wait.until(EC.visibility_of_element_located(PageRegistration.PASSWORD_CONFIRM))
    subs = wait.until(EC.visibility_of_element_located(PageRegistration.SUBSCRIBE))
    assert pass_word.text == "Password"
    assert subs.text == "Subscribe"
