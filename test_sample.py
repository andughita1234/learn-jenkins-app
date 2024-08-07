import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="module")
def browser():
    # Setup: Start a Chrome browser instance
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    # Teardown: Quit the browser after tests
    driver.quit()

def test_google_search(browser):
    # Navigate to Google
    browser.get('https://www.google.com')

    # Assert that the title contains "Google"
    assert "Google" in browser.title, "Title does not contain 'Google'"

    # Find the search box element
    search_box = browser.find_element(By.NAME, 'q')

    # Assert that the search box is displayed
    assert search_box.is_displayed(), "Search box is not displayed"

    # Type in a query and hit ENTER
    search_box.send_keys('OpenAI')
    search_box.submit()

    # Wait for the results to load and check if the title contains "OpenAI"
    browser.implicitly_wait(5)
    assert "OpenAI" in browser.title, "Search results page title does not contain 'OpenAI'"

def test_basic_assertions():
    # Some basic Python assertions
    assert 1 == 1, "1 should be equal to 1"
    assert "hello".upper() == "HELLO", "String should be converted to upper case"
    assert len([1, 2, 3]) == 3, "List length should be 3"

def test_fail():
    # An example of a failing test (You can remove or keep it to see the failure)
    assert 1 == 2, "This test is supposed to fail"

def test_arithmetic():
    # Basic arithmetic checks
    assert 2 + 2 == 4, "2 + 2 should equal 4"
    assert 10 - 3 == 7, "10 - 3 should equal 7"
    assert 3 * 3 == 9, "3 * 3 should equal 9"
    assert 10 / 2 == 5, "10 / 2 should equal 5"

def test_list_operations():
    # Tests related to list operations
    a = [1, 2, 3]
    b = a
    c = a.copy()

    # Test list equality
    assert a == b, "List a should equal list b (same reference)"
    assert a == c, "List a should equal list c (different reference, same content)"

    # Test list content
    assert a[0] == 1, "First element should be 1"
    assert a[-1] == 3, "Last element should be 3"

    # Modify the list and test again
    a.append(4)
    assert a[-1] == 4, "Last element should be 4 after append"
    assert len(a) == 4, "List length should be 4 after append"
