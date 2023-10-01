#!/bin/python3

import math
import os
import random
import re
import sys

def birthday(s, d, m):
    count = 0
    n = len(s)

    # Handle the case when m is greater than the length of s
    if m > n:
        return 0

    for i in range(n - m + 1):
        if sum(s[i:i+m]) == d:
            count += 1

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
