import math
from decimal import Decimal

a, b = list(input().split())

num = math.floor(Decimal(a) * Decimal(b))
print(num)
