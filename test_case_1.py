import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_search_for_flights(browser):
    browser.get("https://www.booking.com")
    source_city = browser.find_element_by_name("ss")
    source_city.send_keys("New York")
    destination_city = browser.find_element_by_name("ss")
    destination_city.send_keys(Keys.DOWN)
    destination_city.send_keys(Keys.ENTER)
    departure_date = browser.find_element_by_css_selector(".xp__input-group .--checkin-field")
    departure_date.clear()
    departure_date.send_keys("2023-09-20")
    search_button = browser.find_element_by_css_selector(".sb-searchbox__button")
    search_button.click()
    time.sleep(5)  
    assert "Search Results" in browser.page_source
