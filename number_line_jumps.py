#!/bin/python3

import math
import os
import random
import re
import sys

def kangaroo(x1, v1, x2, v2):
    # If kangaroo 1 is behind kangaroo 2 and has a smaller or equal jump distance, they will never meet.
    if (x1 < x2 and v1 <= v2) or (x2 < x1 and v2 <= v1):
        return "NO"
    
    # Check if they will land at the same position at the same time
    if (x1 - x2) % (v2 - v1) == 0:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
