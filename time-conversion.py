#!/bin/python3

import os

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Extract hours, minutes, seconds, and AM/PM from the input string
    hours, minutes, seconds, am_pm = int(s[0:2]), int(s[3:5]), int(s[6:8]), s[8:10]

    # Convert to 24-hour format
    if am_pm == "PM" and hours != 12:
        hours += 12
    elif am_pm == "AM" and hours == 12:
        hours = 0

    # Format the result
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

if __name__ == '__main__':
    s = input()
    result = timeConversion(s)
    print(result)
