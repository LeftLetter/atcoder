import math


def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


nums = list(map(int, input().split()))

if nums[0] <= 1 and nums[1] <= 1:
    print(0)
elif nums[1] <= 1:
    print(comb(nums[0], 2))
elif nums[0] <= 1:
    print(comb(nums[1], 2))
else:
    print(comb(nums[0], 2) + comb(nums[1], 2))
