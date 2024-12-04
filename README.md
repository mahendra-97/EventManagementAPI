# EventManagementAPI

## .env File Configurations
DB_NAME = eventmanagementdb
DB_USER = root
DB_PASSWORD = YourPassword
DB_PORT = 3306
DB_HOST = localhost


## Event POST Request input

{
    "event_name":"Myevent3",
    "description":"This is my event",
    "start_time":"2023-11-29 12:00:00",
    "end_time":"2023-11-30 12:00:00",
    "location":"Virtual",
    "max_attendees":100,
    "event_status":"scheduled"
}


## Attendee POST Request input
{
    "first_name":"Mahendra",
    "last_name":"Sonawane",
    "email":"mahendra.sonawane@gmail.com",
    "phone_number":"7894561230",
    "event_id":"2139f439-cb93-467d-ae83-c5cdafcfa262"
    // "check_in_status":""
}