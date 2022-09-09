from selenium.webdriver.common.by import By


class LoginAdminPage:
    USERNAME_INPUT = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    OPENCART_LINK = (By.XPATH, "//*[text()='OpenCart']")
    FORGOTTEN_PASSWORD = (By.LINK_TEXT, "Forgotten Password")
    USERNAME = str("user")
    PASSWORD = str("bitnami")
    ADMIN_PANEL_ONE_ELEMENT = (By.XPATH, "//*[text()='Total Orders ']")
    ADMIN_PANEL_TWO_ELEMENT = (By.XPATH, "//*[text()='Total Sales ']")
    ADMIN_PANEL_THREE_ELEMENT = (By.XPATH, "// *[text() = 'Total Customers ']")
    ADMIN_PANEL_FOUR_ELEMENT = (By.XPATH, "//*[text()=' World Map']")
    ADMIN_PANEL_FIVE_ELEMENT = (By.XPATH, "//*[text()=' Reports']")


class StartPage:
    PHONE_NUMBER = (By.XPATH, "//*[text()='123456789']")
    ADD_TO_CART = (By.XPATH, "//span[text()='Add to Cart']")
    FEATURED = (By.XPATH, "//*[text()='Featured']")
    INFORMATION = (By.XPATH, "//*[text()='Information']")
    LINK_MENU = (By.XPATH, "//*[text()='Tablets']")


class CatalogPage:
    REFINE_SEARCH = (By.XPATH, "//*[text()='Refine Search']")
    ADD_TO_CART_CATALOG = (By.XPATH, "//*[text()='Add to Cart']")
    SHOW_RESULT_ON_PAGE = (By.XPATH, "//*[text()='20']")
    MENU_CATEGORY = (By.XPATH, "//*[text()='Laptops & Notebooks (5)']")
    MENU_CATEGORY_UPPER = (By.XPATH, "//*[text()='MP3 Players']")


class ProductPage:
    TITLE_PRODUCT = (By.XPATH, "//h1[text()='Canon EOS 5D']")
    PRICE_PRODUCT = (By.XPATH, "//h2[text()='$98.00']")
    AVAILABLE_OPTIONS = (By.XPATH, "//h3[text()='Available Options']")
    BRAND = (By.XPATH, "//*[text()='Brand: ']")
    OLD_PRICE = (By.XPATH, "//span[text()='$122.00']")


class PageRegistration:
    FIRST_NAME = (By.XPATH, "//label[text()='First Name']")
    LAST_NAME = (By.XPATH, "//*[text()='Last Name']")
    PASSWORD = (By.XPATH, "//*[text()='Password']")
    PASSWORD_CONFIRM = (By.XPATH, "//label[text()='Password Confirm']")
    SUBSCRIBE = (By.XPATH, "//label[text()='Subscribe']")








    


