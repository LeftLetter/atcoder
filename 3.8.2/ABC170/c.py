x, n = list(map(int, input().split()))


if n == 0:
    print(x)
else:
    pn = list(map(int, input().split()))
    for i in range(x + 1):
        if x - i not in pn:
            print(x - i)
            break
        elif x + i not in pn:
            print(x + i)
            break
    else:
        print(-1)
