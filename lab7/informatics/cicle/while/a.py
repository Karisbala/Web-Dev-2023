n = int(input())
number = 1
while number <= n:
    if int(number**0.5)**2 == number:
        print(number)
    number += 1