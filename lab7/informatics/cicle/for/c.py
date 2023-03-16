number1 = int(input())
number2 = int(input())

for number in range(number1, number2 + 1):
    if int(number**0.5)**2 == number:
        print(number, end = " ")