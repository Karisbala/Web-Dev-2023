n = int(input())
numbers_list = list(map(int, input().split()))
cnt = 0

for i in range(1, n - 1):
    if numbers_list[i] > numbers_list[i-1] and numbers_list[i] > numbers_list[i+1]:
        cnt += 1

print(cnt)