#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())

    for N in range(n):
        S = input()
        print(S[::2], S[1::2])
