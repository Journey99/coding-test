# 수 찾기

def find(a, x):
        start = 0
        end = len(a) - 1

        while start <= end:
            mid = (start + end) // 2

            if x == a[mid]:
                return 1
            elif x > a[mid]:
                start = mid + 1
            else:
                end = mid - 1
        return 0


n = int(input())
A = list(map(int, input().split()))
A.sort()
m = int(input())
X = list(map(int, input().split()))

for i in range(m):
    print(find(A, X[i]))
