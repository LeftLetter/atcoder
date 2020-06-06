a, b, c, d = list(map(int, input().split()))

taka = a
aoki = c

while True:
    aoki -= b
    if aoki <= 0:
        print('Yes')
        break
    taka -= d
    if taka <= 0:
        print('No')
        break
