import sys
def input():
    return sys.stdin.readline()[:-1]

n = int(input())
a_list = list(map(int, input().split()))

a_list.sort()
results = [0] * n

for a in a_list:
    results[a - 1] += 1

for row in results:
    print(row)