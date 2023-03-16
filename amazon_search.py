from selenium.webdriver.common.by import By
from behave import given, when, then

#uppercase for locators)
AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.ID, 'nav-search-submit-button')


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Input text matcha')
def input_search_word(context):
    context.driver.find_element(*AMAZON_SEARCH_FIELD).send_keys('matcha')

# #could also do below example if there are similar inputs but just different words
# # @when('Input text {search_word}')
# def input_search_word(context, search_word):
#     context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(search_word)



@when('Click on search button')
def click_search(context):
    context.driver.find_element(*SEARCH_ICON).click()


@then('Verify that text "matcha" is shown')
def verify_search_result(context):
    expected_result = '"matcha"'
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'



# good to use for search results, registrations(username and password)
# To make scenarios that are all similar, just use scenario outlines
# Scenario Outline: User can search for coffee on Amazon
#     Given Open Amazon page
#     When Input text <search_word>
#     And Click on search button
#     Then Verify that text <search_result> is shown
#     Examples:
#     |search_word  |search_result  |
#     |coffee       |"coffee"       |
#     |table        |"table"        |
#     |mug          |"mug"          |