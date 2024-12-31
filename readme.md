# Work Calendar iCalendar Generator

This project accesses and converts a proprietary work schedule to a .ical to be added to another calendar app using selenium, seleniumwire and python.

Access credentials along with some endpoint information are stored in a local config.json file for privacy purposes, but it's formatted like this:
```
{
    "login_url": "https://placeholder.com/",
    "username": "user",
    "password": "password",
    "username_field_id": "username",
    "password_field_id": "password",
    "schedule_link_id": "ScheduleLink",
    "target_url": "/schedule/events"
}
```
