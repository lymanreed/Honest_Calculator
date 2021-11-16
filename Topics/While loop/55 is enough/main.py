numbers = []
stop = 55
while True:
    number = int(input())
    if number == stop:
        break
    numbers.append(number)
print(len(numbers))
print(sum(numbers))
print(round(sum(numbers) / len(numbers)))
