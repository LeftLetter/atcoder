import io
import sys

if "debugpy" in sys.modules:
    input_data = """\
    """
    sys.stdin = io.StringIO(input_data)


def input():
    return sys.stdin.readline()[:-1]


s = input()
n = int(input())
k = int(input())
n, k = map(int, input().split())
al = list(map(int, input().split()))
cl = list(map(int, input().split()))
