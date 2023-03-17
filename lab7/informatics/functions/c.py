def xor(x, y):
    if x == y:
        return 0
    else:
        return 1
    
numbers = list(map(int, input().split(" ")))
print(xor(numbers[0], numbers[1]))