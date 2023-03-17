n = int(input())
number = 2
while number <= n:
    if n % number == 0:
        print(number)
        break
    number += 1