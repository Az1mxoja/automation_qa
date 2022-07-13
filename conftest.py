# Fixture webdriverni ishga tushirish va dastur so'ngida yopish uchun qo'llaniladi.
# The fixture is used to start the webdriver and close it at the end of the application.
# Fixture используется для запуска веб-драйвера и закрытия его в конце приложения.

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield driver
    driver.quit()
