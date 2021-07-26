import sys
import io


if "debugpy" in sys.modules:
    input_data = """\
3
010
    """
    sys.stdin = io.StringIO(input_data)


def input():
    return sys.stdin.readline()[:-1]


n = int(input())
s = input()

for i, card in enumerate(s):
    if card == "1":
        if i % 2 == 0:
            print("Takahashi")
            break
        else:
            print("Aoki")
            break
