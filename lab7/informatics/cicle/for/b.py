number1 = int(input())
number2 = int(input())
number3 = int(input())
number4 = int(input())

for number in range(number1, number2 + 1):
    if number % number4 == number3:
        print(number, end = " ")