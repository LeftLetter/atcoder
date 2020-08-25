n = input()

n_sum = 0
for ns in n:
    n_sum += int(ns)

if n_sum % 9 == 0:
    print('Yes')
else:
    print('No')
