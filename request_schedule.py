import requests
import json

def get_schedule_xml(cookies):
    # Load configuration from a config file

    config_file = "config.json"  # MAKE SURE THIS IS IN GITIGNORE
    with open(config_file, "r") as file:
        config = json.load(file)

    request_url = config["request_url"]
    request_data = config["request_data"]
    session = requests.Session()
    for cookie in cookies:
        session.cookies.set(cookie['name'], cookie['value'])
    
    response = session.post(request_url, data=request_data)
    if response.status_code == 200:
        return response.text
    else:
        print("Failed to retrieve schedule.")
        return None
