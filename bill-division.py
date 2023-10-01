#!/bin/python3

import math
import os
import random
import re
import sys

def bonAppetit(bill, k, b):
    total_cost = sum(bill)
    anna_share = (total_cost - bill[k]) // 2

    if b == anna_share:
        print("Bon Appetit")
    else:
        print(b - anna_share)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
