def test_hello_selenium(driver):
    driver.get(url="http://192.168.8.103:8081/")
    assert driver.title == "Your Store"


def test_hello_selenium2(driver):
    driver.get(url="http://192.168.8.103:8081/")
    #driver.save_screenshot("test.png")
    assert driver.title == "YourStore"
