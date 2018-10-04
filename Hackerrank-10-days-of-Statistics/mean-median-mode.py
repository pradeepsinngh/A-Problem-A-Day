# Find Mean, Median and Mode

import numpy as np 
from scipy import stats

n = int(input())
x = list(map(int,input().split()))

print(np.mean(x))
print(np.median(x))
print(int(stats.mode(x)[0]))
