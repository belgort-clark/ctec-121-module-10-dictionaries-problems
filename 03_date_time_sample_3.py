# CTEC 121
# 03_date_time_sample_3.py

# import datetime library and timedelta library
from datetime import datetime, timedelta

# import the calendar library
import calendar

# current date time of this computer
now = datetime.now()

testDate = now + timedelta(days=2)

# 2 days from now
print(testDate)

# 3 Weeks ago
longAgo = now - timedelta(weeks=3)
print(longAgo.date())

# Seeing if one date is older than the other
if testDate > longAgo:
    print("testDate is after longAgo")

# Create cal for July, 2001
cal = calendar.month(2001, 7)

# Display calendar
print(cal)

# What day of week was this?
# counting starts with 0. Weeks start with Monday
cal2 = calendar.weekday(2001, 7, 2)
print(cal2)

# Check for leap year
# Returns true or false
cal3 = calendar.isleap(2021)
print(cal3)
