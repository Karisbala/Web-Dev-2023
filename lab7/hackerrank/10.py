if __name__ == '__main__': #Find the Runner-Up Score!
    n = int(input())
    arr = map(int, input().split())
    arr = list(set(list(arr)))
    ar = len(arr)
    arr = sorted(arr)
    print(arr[ar-2])