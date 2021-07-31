import io
import sys

if "debugpy" in sys.modules:
    input_data = """\
9012
    """
    sys.stdin = io.StringIO(input_data)


def input():
    return sys.stdin.readline()[:-1]


s = input()
x1 = int(s[0])
x2 = int(s[1])
x3 = int(s[2])
x4 = int(s[3])

if x1 == x2 == x3 == x4:
    print("Weak")
elif (x1 + 1 == x2 or (x1 == 9 and x2 == 0)) and (x2 + 1 == x3 or (x2 == 9 and x3 == 0)) and (x3 + 1 == x4 or (x3 == 9 and x4 == 0)):
    print("Weak")
else:
    print("Strong")
