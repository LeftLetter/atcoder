n = int(input())
a_list = list(map(int, input().split()))

if 0 in a_list:
    print(0)
else:
    result = 1
    for a in a_list:
        result = result * a
        if result > 10 ** 18:
            print(-1)
            break
    else:
        print(result)
