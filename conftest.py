import pytest

import os
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="firefox", help="browser to run test"
    )


@pytest.fixture()
def driver(request):
    browser_name = request.config.getoption("--cmdopt")

    if browser_name == "chrome":
        _driver = webdriver.Chrome(executable_path=os.path.expanduser("~/Documents/otus/drivers/chromedriver"))
    elif browser_name == "firefox":
        _driver = webdriver.Firefox(executable_path=os.path.expanduser("~/Documents/otus/drivers/geckodriver"))
    elif browser_name == "yandex":
        _driver = webdriver.Chrome(executable_path=os.path.expanduser("~/Documents/otus/drivers/yandexdriver"))
    else:
        raise ValueError(f"Browser {browser_name} is not support")


    yield _driver

    _driver.close()
