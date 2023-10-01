#!/bin/python3

import math
import os
import random
import re
import sys

def plusMinus(arr):
    positive_count = 0
    negative_count = 0
    zero_count = 0
    total_count = len(arr)

    for num in arr:
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
        else:
            zero_count += 1

    # Calculate and print the ratios with 6 decimal places
    print(f"{positive_count / total_count:.6f}")
    print(f"{negative_count / total_count:.6f}")
    print(f"{zero_count / total_count:.6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
