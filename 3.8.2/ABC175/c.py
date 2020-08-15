import sys
input = sys.stdin.readline

x, k, d = map(int, input().split())

a = abs(x) // d
b = abs(x) // d + 1

if a > k:
    print(abs(x) - k * d)
else:
    if b < a:
        a = b

    if (k - a) % 2 == 0:
        print(abs(x) - a * d)
    else:
        print(min(abs(abs(x) - a * d + d), abs(abs(x) - a * d - d)))
