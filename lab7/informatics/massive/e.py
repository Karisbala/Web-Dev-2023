n = int(input())
numbers_list = list(map(int, input().split()))
cnt = 0

for i in range(1, n):
    if numbers_list[i] * numbers_list[i-1] >= 0:
        cnt = 1

if cnt == 1:
    print("YES")
else:
    print("NO")