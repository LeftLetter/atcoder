import sys
import itertools
input = sys.stdin.readline

n = int(input())
l_list = list(map(int, input().split()))
p_list = list(itertools.permutations(l_list, 3))
p_list = list(filter(lambda e: len(set(e)) == len(e), p_list))

if len(p_list) < 3:
    print(0)
else:
    count = 0
    for p in p_list:
        if p[0] < p[1] < p[2] and p[2] < p[0] + p[1]:
            count += 1
    print(count)
