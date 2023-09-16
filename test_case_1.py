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
    destination_city = browser.find_element_by_name("ss")
    departure_date = browser.find_element_by_css_selector(".xp__input-group .--checkin-field")
    search_button = browser.find_element_by_css_selector(".sb-searchbox__button")
    source_city_input = "New York"
    destination_option_index = 1 
    departure_date_input = "2023-09-20"
    source_city.send_keys(source_city_input)
    destination_city.send_keys(Keys.DOWN)
    destination_city.send_keys(Keys.ENTER)
    departure_date.clear()
    departure_date.send_keys(departure_date_input)
    search_button.click()
    
    time.sleep(5)
    assert "Search Results" in browser.page_source
