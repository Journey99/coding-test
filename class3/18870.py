n = int(input())
arr = list(map(int, input().split()))

sort_arr = sorted(list(set(arr)))
dic = { sort_arr[i] : i for i in range(len(sort_arr))}
for i in arr:
    print(dic[i], end = " ")

# set함수는 중복되는 원소를 제거하고 집합을 만든다.