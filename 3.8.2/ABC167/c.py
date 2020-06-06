import itertools

n, m, x = list(map(int, input().split()))
all_list = []
for i in range(n):
    tmp = list(map(int, input().split()))
    all_list.append(tmp)

ok = False
cur_price = (10 ** 5) * n + 1
for i in range(1, n + 1):
    answers = list(itertools.combinations(range(n), i))
    # print(answers)
    for ans_list in answers:
        sum_list = [0] * (m + 1)
        # print(sum_list)
        for ans in ans_list:
            # print(all_list[int(ans[0])])
            sum_list = [a + b for a, b in zip(sum_list, all_list[int(ans)])]
        # print(sum_list)
        if min(sum_list[1:]) >= x:
            if sum_list[0] < cur_price:
                cur_price = sum_list[0]
                ok = True

if ok:
    print(cur_price)
else:
    print(-1)
