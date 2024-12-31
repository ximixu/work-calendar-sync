from seleniumrequests import Chrome
import json

def get_schedule_xml(driver):
    # Load configuration from a config file

    config_file = "config.json"  # MAKE SURE THIS IS IN GITIGNORE
    with open(config_file, "r") as file:
        config = json.load(file)

    request_url = config["request_url"]
    request_data = config["request_data"]
    
    response = driver.request('POST', request_url, json = request_data)
    if response.status_code == 200:
        return response.text
    else:
        print("Failed to retrieve schedule.")
        return None
