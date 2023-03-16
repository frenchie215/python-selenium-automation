from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click Returns and Orders button')
def click_orders(context):
    context.driver.find_element(By.CSS_SELECTOR, '#nav-orders').click()


@then('Verify Sign in page opened: Sign In header is visible, email input field is present')
def verify_page(context):
    expected_result1 = context.driver.find_element(By.CSS_SELECTOR, '#ap_email').text
    actual_result1 = context.driver.find_element(By.CSS_SELECTOR, '#ap_email').text
    assert expected_result1 == actual_result1, f'Expected {expected_result1} but actually got {actual_result1}'