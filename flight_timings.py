from datetime import datetime, timedelta
import pytz

# Define the time zones
india_tz = pytz.timezone('Asia/Kolkata')
pittsburgh_tz = pytz.timezone('America/New_York')

# Get the departure date and time from India
departure_date_str = input("Enter the departure date from India (YYYY-MM-DD): ")
departure_time_str = input("Enter the departure time from India (HH:MM): ")
departure_datetime = india_tz.localize(datetime.strptime(f"{departure_date_str} {departure_time_str}", "%Y-%m-%d %H:%M"))

# Get the duration of the journey
duration_hours = int(input("Enter the duration of the journey in hours: "))
duration_minutes = int(input("Enter the duration of the journey in minutes: "))
journey_duration = timedelta(hours=duration_hours, minutes=duration_minutes)

# Calculate the arrival date and time in Pittsburgh
arrival_datetime = departure_datetime + journey_duration
anarrival_datetime_pittsburgh = arrival_datetime.astimezone(pittsburgh_tz)

# Get the arrival time in Pittsburgh
'''arrival_time_str = input("Enter the scheduled arrival time in Pittsburgh (HH:MM): ")
arrival_time = datetime.strptime(arrival_time_str, "%H:%M").time()

# Adjust the arrival date and time to match the scheduled arrival time
arrival_datetime_pittsburgh = arrival_datetime_pittsburgh.replace(hour=arrival_time.hour, minute=arrival_time.minute)
'''

# Print the arrival date and time in Pittsburgh
print(f"The flight will land in Pittsburgh on {arrival_datetime_pittsburgh.strftime('%Y-%m-%d %H:%M')}")