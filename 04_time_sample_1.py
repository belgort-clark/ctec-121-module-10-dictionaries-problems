# CTEC 121
# 04_time_sample_1.py

import time

print("Enter 'Yes' to begin")
run = input("Start? > ").lower()

seconds = 10

if run == "yes":
    # Keep looping until seconds != 10
    while seconds > -1:
        print(">", seconds)
        # sleep for one second
        time.sleep(1)
        # increase seconds by 1
        seconds -= 1
    print('Boom')
