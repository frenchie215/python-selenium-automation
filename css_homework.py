from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


driver = webdriver.Chrome(executable_path='/Users/francesgibson/Desktop/Automation/chromedriver')


driver.find_element(By.CSS_SELECTOR, 'i.a-icon.a-icon-logo')
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')
driver.find_element(By.CSS_SELECTOR, '#ap_email')
driver.find_element(By.CSS_SELECTOR, '#ap_password')
driver.find_element(By.CSS_SELECTOR, "div[class*='a-alert-content']")
driver.find_element(By.CSS_SELECTOR, '.a-box-inner.a-alert-container')
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')
 '#continue')
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")
driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")
driver.find_element(By.CSS_SELECTOR, 'a.a-link-emphasis')'