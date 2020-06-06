n, m = list(map(int, input().split()))
a_list = list(map(int, input().split()))

homework_sum = sum(a_list)
if homework_sum > n:
    print(-1)
else:
    print(n - homework_sum)
