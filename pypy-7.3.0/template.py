import sys
import io


if "debugpy" in sys.modules:
    input_data = """\
    """
    sys.stdin = io.StringIO(input_data)


def input():
    return sys.stdin.readline()[:-1]


n = input()
k = int(input())
n, k = map(int, input().split())
a_list = list(map(int, input().split()))
