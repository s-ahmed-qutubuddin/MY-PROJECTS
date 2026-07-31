import pytz
from datetime import datetime
import time
import os

alarm_time=input("Enter your preferred time (HH:MM:SS) or (HH:MM) format:")
print(alarm_time)
zone=input("Enter your timezone: ")
try:
    timezone=pytz.timezone(zone)
except pytz.exceptions.UnknownTimeZoneError:
    print("Invalid timezone. Please) enter a valid timezone.")
print(timezone)
print(datetime.now(timezone))

while True:
    current_time=datetime.now(timezone).strftime("%H:%M:%S")
    print(current_time)
    if current_time==alarm_time:
        os.system("afplay /System/Library/Sounds/Glass.aiff")
        print("wake up")
        break
    time.sleep(1)
        
