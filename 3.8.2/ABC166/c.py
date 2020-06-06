n, m = list(map(int, input().split()))
h = list(map(int, input().split()))

count = 0
good_list = [i for i in range(1, n + 1)]
bad_list = []
for i in range(m):
    a, b = list(map(int, input().split()))

    if h[a - 1] < h[b - 1]:
        bad_list.append(a)
    elif h[a - 1] > h[b - 1]:
        bad_list.append(b)
    else:
        bad_list.append(a)
        bad_list.append(b)

print(len(set(good_list) - set(bad_list)))
