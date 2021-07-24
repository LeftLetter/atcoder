import sys
import io
import math


def input():
    if "debugpy" in sys.modules:
        input_data = """\
11 10 9
        """
        sys.stdin = io.StringIO(input_data)
    return sys.stdin.readline()[:-1]


a, b, n = map(int, input().split())

x = min(b - 1, n)
result = math.floor(a * x / b) - a * math.floor(x / b)


# max = 0
# for x in range(0, n + 1):
#     cand = math.floor(a * x / b) - a * math.floor(x / b)
#     if cand < max:
#         break
#     max = cand
#     print(x, cand)
print(result)
