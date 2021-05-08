t = int(input())


for i in range(t):
    k = int(input())
    n = int(input())
    arr=[[0 for i in range(n)]for i in range(k+1)]

    for q in range(n): #0층의 인원수 채우기.
        arr[0][q] = q+1

    for j in range(1,k+1): #0층의 인원수를 더해 1층...2층.... 쌓아가는 반복문
        for z in range(n):
            arr[j][z] += sum(arr[j-1][:z+1])

    print(arr[k][n-1])