from decimal import *
x = int(input())

year = 0
money = 100
while True:
    money = Decimal(money) * Decimal(1.01) // Decimal(1)
    year += 1
    if money >= x:
        print(year)
        break
