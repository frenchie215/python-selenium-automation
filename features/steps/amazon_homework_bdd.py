from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click Returns and Orders button')
def click_orders(context):
    context.driver.find_element(By.CSS_SELECTOR, '#nav-orders')


@then('Verify Sign in page opened: Sign In header is visible, email input field is present')
def verify_page(context):
    expected_result = 'Sign In'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, '#ap_email')
    assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'