import sys

T = int(sys.stdin.readline())
arr = []

for i in range(41):
    if i == 0:
        arr.append([1, 0])
    elif i == 1:
        arr.append([0, 1])
    else:
        arr.append([arr[i-1][0] + arr[i-2][0], arr[i-1][1] + arr[i-2][1]])

for _ in range(T):
    num = int(sys.stdin.readline())
    print(arr[num][0], arr[num][1])