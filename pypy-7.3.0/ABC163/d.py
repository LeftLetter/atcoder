import sys
import io


def input():
    if "debugpy" in sys.modules:
        input_data = """\
141421 35623
        """
        sys.stdin = io.StringIO(input_data)
    return sys.stdin.readline()[:-1]


n, k = map(int, input().split())
mod = 10 ** 9 + 7
result = 0

for i in range(k, n + 2):
    min = i * (i - 1) / 2
    # min = 0
    # for j in range(i):
    #     min += j
    max = i * (2 * n - i + 1) / 2
    # max = 0
    # for j in range(n, n - i, -1):
    #     max += j

    result += max - min + 1

print(int(result % mod))
