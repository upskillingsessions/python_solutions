#!/bin/python3

import math
import os
import random
import re
import sys

def sockMerchant(n, ar):
    color_counts = {}  # Dictionary to store the count of each color

    # Count the occurrences of each color
    for color in ar:
        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1

    # Calculate the number of pairs for each color
    pairs = 0
    for count in color_counts.values():
        pairs += count // 2

    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
