import io
import sys

if "debugpy" in sys.modules:
    input_data = """\
        50 50
    """
    sys.stdin = io.StringIO(input_data)


def input():
    return sys.stdin.readline()[:-1]


a, b = map(int, input().split())

if 0 < a and b == 0:
    print("Gold")
elif a == 0 and 0 < b:
    print("Silver")
else:
    print("Alloy")
