# CTEC 121
# 02_date_time_sample_2.py

# import datetime library
from datetime import datetime

# current date time of this computer
now = datetime.now()

# %a shortened day of the week name
# %A long day of week the week name
# %d is the day number
# %m is the month number
# %b is the month abbreviation
# %B is the full month name
# %y is the years last two digits
# %Y is the full year

# Fri Friday 03 06 2020
print(now.strftime('%a %A %d %y %Y'))
# March 6, 2020
print("{:%B %d, %Y}".format(now))

# Now for time
# %H for hours
# %M for minutes
# %S for seconds
# %p for AM or PM
print(now.strftime('%H %M %S %p'))
