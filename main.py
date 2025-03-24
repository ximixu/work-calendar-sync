import login
import json_to_ical
import os

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    schedule_path = os.path.join(base_dir, "schedule.json")
    login.get_schedule()
    json_to_ical.convert(schedule_path)

if __name__ == "__main__":
    main()