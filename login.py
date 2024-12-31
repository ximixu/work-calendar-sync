from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import gzip

# Load configuration from a config file
config_file = "config.json"  # MAKE SURE THIS IS IN GITIGNORE
with open(config_file, "r") as file:
    config = json.load(file)

login_url = config["login_url"]
username = config["username"]
password = config["password"]
username_field_id = config["username_field_id"]
password_field_id = config["password_field_id"]
schedule_link_id = config["schedule_link_id"]
target_url = config["target_url"]

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

def get_schedule():
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(login_url)
        WebDriverWait(driver, 20).until(EC.url_changes(login_url))

        username_field = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, username_field_id))
        )
        username_field.send_keys(username)
        username_field.send_keys(Keys.RETURN)

        password_field = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, password_field_id))
        )
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)

        schedule_link = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, schedule_link_id))
        )
        schedule_link.click()

        schedule_request = driver.wait_for_request(target_url, 60)
        schedule = gzip.decompress(schedule_request.response.body)
        schedule_json = json.loads(schedule.decode('utf-8'))

        print(schedule_json)
        
        with open('schedule.json', 'w') as file:
            json.dump(schedule_json, file, indent=4)

        driver.quit()

    except Exception as e:
        driver.quit()
        raise e

if __name__ == "__main__":
    get_schedule()