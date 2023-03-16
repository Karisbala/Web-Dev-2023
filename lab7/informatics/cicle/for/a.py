number1 = int(input())
number2 = int(input())
for number in range(number1, number2 + 1):
    if number % 2 == 0:
        print(number, end = ' ')