n = int(input())
numbers_list = list(map(int, input().split()))

for i in range(0, n):
    if numbers_list[i] % 2 == 0:
        print(numbers_list[i], end = " ")
