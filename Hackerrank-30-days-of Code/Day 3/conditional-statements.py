#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())

if n%2 != 0:
    print('Weird')
elif n%2 == 0 and n < 6 and n > 1:
    print('Not Weird')
elif n%2 == 0 and n > 5 and n < 21:
    print('Weird')
elif n%2 == 0 and n > 20:
    print('Not Weird')
