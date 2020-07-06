n = int(input())

ss = []
for s in range(n):
    ss.append(input())

print(f'AC x {ss.count("AC")}')
print(f'WA x {ss.count("WA")}')
print(f'TLE x {ss.count("TLE")}')
print(f'RE x {ss.count("RE")}')
