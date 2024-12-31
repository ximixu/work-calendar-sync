from icalendar import Calendar, Event
from datetime import datetime
import pytz
import json

def convert(json_file):
    # Load the JSON schedule
    with open(json_file, "r") as file:
        schedule = json.load(file)

    regular_shifts = schedule.get("regularShifts", [])

    # Assuming JSON uses local time without timezone info
    local_timezone = pytz.timezone("US/Pacific")
    cal = Calendar()

    for shift in regular_shifts:
        # Parse local times from JSON
        start = datetime.fromisoformat(shift["startDateTime"])
        end = datetime.fromisoformat(shift["endDateTime"])
        
        # convert to UTC
        start_utc = local_timezone.localize(start).astimezone(pytz.UTC)
        end_utc = local_timezone.localize(end).astimezone(pytz.UTC)
        
        # Create an event
        event = Event()
        event.add('summary', "Work Shift")
        event.add('dtstart', start_utc)  # UTC format
        event.add('dtend', end_utc)  # UTC format
        event.add('description', "Regular work shift")
        event.add('location', "Workplace")
        
        cal.add_component(event)

    # Write the .ics file
    with open("schedule.ics", "wb") as f:
        f.write(cal.to_ical())

    print("ICS file created: schedule.ics")

if __name__ == "__main__":
    convert("schedule.json")