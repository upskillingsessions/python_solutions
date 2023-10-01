#!/bin/python3

import math
import os
import random
import re
import sys

def superReducedString(s):
    stack = []  # Create an empty stack to store characters
    
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()  # Pop if there's a match
        else:
            stack.append(char)  # Otherwise, push the character onto the stack
    
    reduced_string = ''.join(stack)  # Join the remaining characters in the stack
    
    if not reduced_string:
        return "Empty String"
    else:
        return reduced_string

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
