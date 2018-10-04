#!/bin/python3

import math
import os
import random
import re
import sys

def solve(s):
    l=s.split(" ")
    a = [i.capitalize() for i in l]       
    return " ".join(a)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
