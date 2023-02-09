from selenium import webdriver
from selenium.webdriver.common.by import By


#example reference
#driver.find_element(By.XPATH, "//input[@placeholder='Search Amazon']")


driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")
driver.find_element(By.ID, "//input[@id='continue']")
driver.find_element(By.XPATH, "//span[contains(@class, 'a-expander-prompt')]")
driver.find_element(By.ID, "//a[@id='auth-fpp-link-bottom']")
driver.find_element(By.ID, "//a[@id='ap-other-signin-issues-link']")
driver.find_element(By.ID, "//a[@id='createAccountSubmit']")
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")
driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")
##