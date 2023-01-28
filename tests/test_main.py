"""
2023 - test
"""
from selenium.webdriver.common.by import By

URL = 'https://testqastudio.me/'

def test_smoke(browser):
    """
    SMK-1 Smoke test
    """
    browser.get(URL)
    element = browser.find_element(by=By.CSS_SELECTOR, value="[class='tab-featured ']")
    element.click()
    xpath_table = '//*[@id="rz-shop-content"]/ul/li[1]/div/div[2]/h2/a'
    element = browser.find_element(By.XPATH, value= xpath_table)
    element.click()
    sku = browser.find_element(By.CLASS_NAME, value="sku")
    assert sku.text == 'C0MSSDSUM7', "Unxepected sku"
    print('Тест выполнен успешно')
