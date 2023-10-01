#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function is expected to print two space-separated long integers.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    min_sum = float('inf')
    max_sum = 0
    total_sum = sum(arr)

    for num in arr:
        min_sum = min(min_sum, total_sum - num)
        max_sum = max(max_sum, total_sum - num)

    print(min_sum, max_sum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
