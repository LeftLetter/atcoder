import sys
import io


if "debugpy" in sys.modules:
    input_data = """\
        300 50
    """
    sys.stdin = io.StringIO(input_data)


def input():
    return sys.stdin.readline()[:-1]


a, b = map(int, input().split())
print((a - b) / 3.0 + b)
