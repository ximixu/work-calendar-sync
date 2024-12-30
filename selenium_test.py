from selenium import webdriver

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to a website
driver.get("https://www.google.com")

print("Title: ", driver.title)

# Close the browser
driver.quit()
