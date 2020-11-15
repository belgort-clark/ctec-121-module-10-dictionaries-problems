# CTEC 121
# 01_date_time_sample_1.py

# import datetime library
from datetime import datetime

# current date time of this computer
now = datetime.now()

# Print it out
print(now.date())

# Print current year
print(now.year)

# Print current month
print(now.month)

# Print out hour
print(now.hour)

# Print minutes
print(now.minute)

# Print seconds
print(now.second)

# Whole time
print(now.time())
