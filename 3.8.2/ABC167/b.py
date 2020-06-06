a, b, c, k = list(map(int, input().split()))

count = 0

if k <= a:
    print(k)
else:
    count = k - a
    if count <= b:
        print(a)
    else:
        count = count - b
        print(a - count)
