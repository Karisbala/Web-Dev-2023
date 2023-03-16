cnt = 0
n = int(input())
for i in range(1, n + 1):
    number = int(input())
    if number == 0:
        cnt += 1
print(cnt)