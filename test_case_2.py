import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_book_tickets(browser, source_city, departure_date, passenger_name, passenger_age, passenger_gender):
    browser.get("https://www.booking.com")
    source_city_input = browser.find_element(By.NAME, "ss")
    source_city_input.send_keys(source_city)
    time.sleep(2) 
    source_city_input.send_keys(Keys.ARROW_DOWN)
    source_city_input.send_keys(Keys.ENTER)
    departure_date_input = browser.find_element(By.CSS_SELECTOR, "input[name='checkin_monthday']")
    departure_date_input.clear()
    departure_date_input.send_keys(departure_date)
    search_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    search_button.click()
    time.sleep(5)
    sort_by_price_button = browser.find_element(By.XPATH, "//a[@data-category='price']")
    sort_by_price_button.click()
    time.sleep(2)
    select_seats_button = browser.find_element(By.XPATH, "//button[@data-test-id='select-seats-button']")
    select_seats_button.click()
    time.sleep(5)
    passenger_name_input = browser.find_element(By.XPATH, "//input[@name='passenger_name']")
    passenger_name_input.send_keys(passenger_name)
    age_input = browser.find_element(By.XPATH, "//input[@name='age']")
    age_input.send_keys(passenger_age)
    gender_dropdown = browser.find_element(By.XPATH, "//select[@name='gender']")
    gender_dropdown.click()
    ActionChains(browser).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
    continue_button = browser.find_element(By.XPATH, "//button[@data-test-id='passenger-continue-button']")
    continue_button.click()
    assert "Booking confirmation" in browser.page_source

if __name__ == "__main__":
    pytest.main(["-v", __file__, "--browser=chrome", "--source_city=New York", "--departure_date=2023-09-20", "--passenger_name=John Doe", "--passenger_age=30", "--passenger_gender=Male"])
