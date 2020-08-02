import sys
input = sys.stdin.readline

n = int(input())
c = input()

rc = c.count('R')
wc = c.count('W')

if wc == 0 or rc == 0:
    print(0)
else:
    rstr = c[0:rc]
    wstr = c[rc:]
    print(max(rstr.count('W'), wstr.count('R')))
