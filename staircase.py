#!/bin/python3

import math
import os
import random
import re
import sys

def staircase(n):
    for i in range(1, n + 1):
        # Print (n - i) spaces
        spaces = ' ' * (n - i)
        # Print i '#' symbols
        symbols = '#' * i
        # Print the combined string of spaces and symbols
        print(spaces + symbols)

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
