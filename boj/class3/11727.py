# 2xn 타일링2

n = int(input())
arr= [1,3,5]

while(True):
    arr.append(arr[-2]*2 + arr[-1])
    if len(arr) > n : break
print(arr[n-1]%10007)