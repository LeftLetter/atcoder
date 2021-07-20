import sys
def input():
    return sys.stdin.readline()[:-1]

n = input()
k = int(input())
n, k = map(int, input().split())
a_list = list(map(int, input().split()))
