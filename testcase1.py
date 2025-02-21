from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service


service = Service('/Users/francesgibson/Desktop/Automation/chromedriver')
driver = webdriver.Chrome(service=service)

driver.get('https://www.amazon.com/')

driver.find_element(By.XPATH, "//span[text()='& Orders']").click()

sleep(4)


expected_result= '"Sign In"'
actual_result = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']")
print(actual_result)


print('Test Case Passed')

driver.quit()