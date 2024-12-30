from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

# Load configuration from a config file
config_file = "config.json"  # MAKE SURE THIS IS IN GITIGNORE
with open(config_file, "r") as file:
    config = json.load(file)

login_url = config["login_url"]
username = config["username"]
password = config["password"]
username_field_id = config["username_field_id"]
password_field_id = config["password_field_id"]
success_indicator_id = config["success_indicator_id"]

# Set up Chrome options for headless mode
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

try:
    # Navigate to the login page
    driver.get(login_url)

    # Wait for the redirection to the proper URL
    WebDriverWait(driver, 20).until(EC.url_changes(login_url))

    # Wait for the username field to become available
    username_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, username_field_id))
    )

    # Enter username
    username_field.send_keys(username)
    username_field.send_keys(Keys.RETURN)

    # Wait for the password field to become available
    password_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, password_field_id))
    )

    # Locate and fill in the password field
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)

    # Wait for successful login and redirection
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, success_indicator_id))
    )

    # Get cookies
    cookies = driver.get_cookies()
    print("Cookies:")
    for cookie in cookies:
        print(cookie)

finally:
    # Close the browser
    driver.quit()
