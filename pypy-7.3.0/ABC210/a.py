import sys
import io


if "debugpy" in sys.modules:
    input_data = """\
10 10 100 1
    """
    sys.stdin = io.StringIO(input_data)


def input():
    return sys.stdin.readline()[:-1]


n, a, x, y = map(int, input().split())

if n <= a:
    print(n * x)
else:
    print(a * x + (n - a) * y)
