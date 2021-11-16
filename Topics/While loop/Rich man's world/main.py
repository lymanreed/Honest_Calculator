deposit, years, max_deposit, interest = float(input()), 0, 700000, 1.071

while deposit < max_deposit:
    deposit *= interest
    years += 1

print(years)
