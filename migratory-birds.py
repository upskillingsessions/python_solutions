#!/bin/python3

import math
import os
import random
import re
import sys

def migratoryBirds(arr):
    bird_count = {}  # Create a dictionary to count bird occurrences

    for bird in arr:
        if bird in bird_count:
            bird_count[bird] += 1
        else:
            bird_count[bird] = 1

    max_count = 0
    min_id = float('inf')

    for bird, count in bird_count.items():
        if count > max_count or (count == max_count and bird < min_id):
            max_count = count
            min_id = bird

    return min_id

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
