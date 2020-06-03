from decimal import Decimal
nums = list(map(Decimal, input().split()))

if nums[0].sqrt() + nums[1].sqrt() < nums[2].sqrt():
    print('Yes')
else:
    print('No')
