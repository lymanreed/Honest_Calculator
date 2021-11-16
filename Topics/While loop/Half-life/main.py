current, final = int(input()), int(input())
periods = 0
while current >= final:
    current = current / 2
    periods += 1
print(periods * 12)
