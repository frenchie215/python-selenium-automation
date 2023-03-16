from selenium.webdriver.common.by import By
from behave import when, given, then
from time import sleep


ADD_TO_CART_BTN = (By. ID, 'add-to-cart-button')


@when('Click on Add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    sleep(5)

#manually exit out the protection plan if it appears within alloted time