income = int(input())
if income < 15528:
    rate = 0
elif income < 42708:
    rate = 15
elif income < 132407:
    rate = 25
else:
    rate = 28
tax = round(income * (rate / 100))

print(f"The tax for {income} is {rate}%. That is {tax} dollars!")
