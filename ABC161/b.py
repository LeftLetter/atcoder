nm = list(map(int, input().split()))
n = nm[0]
m = nm[1]
an = list(map(int, input().split()))


count = 0
for a in an:
    if a >= sum(an) / (4.0 * m):
        count += 1

if count >= m:
    print('Yes')
else:
    print('No')
