import sys
import io


if "debugpy" in sys.modules:
    input_data = """\
5
3 3 3 3 3
    """
    sys.stdin = io.StringIO(input_data)


def input():
    return sys.stdin.readline()[:-1]


n = int(input())
a_list = list(map(int, input().split()))

sum = 0
max = a_list[0]
for a in a_list:
    if a > max:
        max = a
    elif a < max:
        sum += max - a

print(sum)
