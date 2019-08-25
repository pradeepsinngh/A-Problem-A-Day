#!/bin/python3

import math
import os
import random
import re
import sys

def Factorial(num):
    if num == 1:
        return 1
    else:
        return (num * Factorial(num-1))
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = Factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
