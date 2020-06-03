n, k = list(map(int, input().split()))

sunuke = [i for i in range(1, n + 1)]

for i in range(k):
    d = input()
    a = list(map(int, input().split()))
    for j in a:
        if j in sunuke:
            sunuke.remove(j)
print(len(sunuke))
