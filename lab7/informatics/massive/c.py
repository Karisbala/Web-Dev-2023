n = int(input())
numbers_list = list(map(int, input().split()))
pos = 0

for i in range(0, n):
    if numbers_list[i] > 0:
        pos += 1

print(pos)