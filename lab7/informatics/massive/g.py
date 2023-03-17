n = int(input())
numbers_list = list(map(int, input().split()))
numbers_list = numbers_list[::-1]
for number in numbers_list:
    print(number, end = ' ')
