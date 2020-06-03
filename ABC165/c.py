import itertools

n, m, q = list(map(int, input().split()))
nums = []
for i in range(q):
    nums.append(list(map(int, input().split())))
a = list(itertools.combinations_with_replacement(
    [e for e in range(1, m + 1)], n))
for i in range(len(a)):
    a[i] = sorted(a[i])
results = [0]
for j in range(len(a)):
    max_value = 0
    for i in range(q):
        if a[j][nums[i][1] - 1] - a[j][nums[i][0] - 1] == nums[i][2]:
            max_value += nums[i][3]
    else:
        results.append(max_value)

print(max(results))
