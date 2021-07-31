import io
import sys

if "debugpy" in sys.modules:
    input_data = """\
6 8
17 39 67 2 45 35 22 24 9 45 52 56 48 94 84
82 76 82 82 71 70 40
    """
    sys.stdin = io.StringIO(input_data)


def input():
    return sys.stdin.readline()[:-1]


n, m = map(int, input().split())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))
al.sort()
bl.sort()

len1 = len(al)
len2 = len(bl)
if len1 > len2:
    tmp = bl
    bl = al
    al = tmp

minimum = 10 ** 9 + 1
cur = 0
for i in range(len(al)):
    before_diff = 10 ** 9 + 1
    for j in range(cur, len(bl)):
        diff = abs(al[i] - bl[j])
        if diff <= minimum:
            minimum = diff
        elif diff > before_diff:
            cur = j - 1
            break
        before_diff = diff
    else:
        break

print(minimum)

# minimum = 2 * 10**5 + 1
# for a in al:
#     before_diff = 2 * 10**5 + 1
#     for b in bl:
#         diff = abs(a - b)
#         if diff < minimum:
#             minimum = diff
#         if diff > before_diff:
#             break
#         before_diff = diff

# print(minimum)
