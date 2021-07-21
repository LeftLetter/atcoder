import sys
def input():
    return sys.stdin.readline()[:-1]

import math
from functools import reduce
k = int(input())

sum = 0
for a in range(1, k + 1):
    for b in range(1, k + 1):
        for c in range(1, k + 1):
            sum += reduce(math.gcd, [a, b, c])
print(sum)