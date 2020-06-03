n = int(input())
s = input()

all = s.count('R') * s.count('G') * s.count('B')
max_diff = (n - 3) // 2
for i in range(max_diff + 1):
    for j in range(n - i - i - 2):
        if s[j] != s[j + 1 + i] and s[j] != s[j + 1 + i + 1 + i] and s[j + 1 + i] != s[j + 1 + i + 1 + i]:
            all -= 1
print(all)
