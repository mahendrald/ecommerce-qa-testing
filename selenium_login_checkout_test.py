from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setup
browser = webdriver.Chrome()
browser.get("http://automationpractice.com/index.php")

# Login
browser.find_element(By.CLASS_NAME, "login").click()
time.sleep(2)
browser.find_element(By.ID, "email").send_keys("testuser@example.com")
browser.find_element(By.ID, "passwd").send_keys("Password123")
browser.find_element(By.ID, "SubmitLogin").click()

# Add to cart
browser.find_element(By.CLASS_NAME, "product-name").click()
time.sleep(2)
browser.find_element(By.NAME, "Submit").click()
time.sleep(2)

# Proceed to checkout
browser.find_element(By.CLASS_NAME, "button-medium").click()
time.sleep(2)

# Cleanup
browser.quit()

# ---------------------------
# API_Testing/postman_collection.json

{
  "info": {
    "name": "E-commerce API Tests",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
  },
  "item": []
}

# ------------------------- 
