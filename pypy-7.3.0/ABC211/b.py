import sys
import io


if "debugpy" in sys.modules:
    input_data = """\
2B
3B
HR
3B
    """
    sys.stdin = io.StringIO(input_data)


def input():
    return sys.stdin.readline()[:-1]


s1 = input()
s2 = input()
s3 = input()
s4 = input()

targets = [s1, s2, s3, s4]
if "H" in targets and "2B" in targets and "3B" in targets and "HR" in targets:
    print("Yes")
else:
    print("No")
