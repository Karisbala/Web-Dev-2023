def power(a: float, n: int):
    return a**n

numbers = input().split(" ")
print(power(float(numbers[0]), int(numbers[1])))