import pytest

import os
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="chrome", help="browser to run test"
    )
    parser.addoption(
        "--headless", action="store_true", help="browser to run test"
    )
    parser.addoption(
        "--drivers", default=os.path.expanduser("~/Documents/otus/drivers")
    )
    parser.addoption(
        "--base_url", default="http://192.168.8.103:8081/"
    )


@pytest.fixture()
def driver(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    drivers_source = request.config.getoption("--drivers")
    base_url = request.config.getoption("--base_url")

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.headless = True
        _driver = webdriver.Chrome(
            executable_path=os.path.expanduser(f"{drivers_source}/chromedriver"),
            options=options
        )
    elif browser_name == "firefox":
        _driver = webdriver.Firefox(executable_path=os.path.expanduser(f"{drivers_source}/geckodriver"))
    elif browser_name == "yandex":
        _driver = webdriver.Chrome(executable_path=os.path.expanduser(f"{drivers_source}/yandexdriver"))
    else:
        raise ValueError(f"Browser {browser_name} is not support")

    _driver.base_url = base_url
    yield _driver

    _driver.close()
