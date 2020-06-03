nk = list(map(int, input().split()))
n = nk[0]
k = nk[1]

a = n % k
b = abs(a - k)

if a < b:
    print(a)
else:
    print(b)
