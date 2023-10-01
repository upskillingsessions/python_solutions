#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    sea_level = 0
    valley_count = 0

    for step in path:
        if step == 'U':
            sea_level += 1
        elif step == 'D':
            sea_level -= 1

        # Check if we have just exited a valley
        if step == 'U' and sea_level == 0:
            valley_count += 1

    return valley_count

if __name__ == '__main__':
    steps = int(input().strip())
    path = input()

    result = countingValleys(steps, path)
    print(result)
