import login
import json_to_ical

def main():
    login.get_schedule()
    json_to_ical("schedule.json")

if __name__ == "__main__":
    main()