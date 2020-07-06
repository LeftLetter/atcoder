import itertools
import copy
h, w, k = map(int, input().split())

cs = []
for i in range(h):
    cs.append(list(input()))

# print(cs)

hpatterns = []
for i in range(h + 1):
    hpatterns += list(itertools.combinations(range(h), i))
wpatterns = []
for i in range(w + 1):
    wpatterns += list(itertools.combinations(range(w), i))

# print(hpatterns)
# print(wpatterns)

c = 0
for hpattern in hpatterns:
    for wpattern in wpatterns:
        black = 0
        cs2 = copy.deepcopy(cs)
        for pi in hpattern:
            cs2[pi] = ['' for k in range(w)]

        for pj in wpattern:
            for s in range(len(cs2)):
                # print(pj, s)
                cs2[s][pj] = ''
        # print(wpattern, hpattern, cs2)
        for s in cs2:
            black += s.count('#')

        if black == k:
            c += 1

print(c)
