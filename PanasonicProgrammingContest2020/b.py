import math
nums = list(map(int, input().split()))

cell = nums[0] * nums[1]

if nums[0] == 1 or nums[1] == 1:
    print(1)
elif cell % 2 == 0:
    print(int(cell / 2))
else:
    print(int(math.ceil(cell / 2)))
