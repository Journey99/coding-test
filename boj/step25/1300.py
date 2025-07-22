# k번째 수
'''
시간복잡도 : O(nlogk)
해결 방법 : 어떤 수 mid를 기준으로, 곱셈표안에 mid보다 작거나 같은 값이 몇 개 있는지를 세어야한다
-> i 행의 값 : i, 2i, 3i, ,, ni
-> i * j <= mid 를 만족하는 j의 개수를 찾아야 함
-> j <= mid // i 
-> mid // i 가 n보다 커질 수 있기 때문에 i행에서 mid 이하인 수의 개수 = min(mid // i, n)

'''

n = int(input())
k = int(input())

start = 1
end = k
answer = 0

while start <= end:
    mid = (start+end)//2

    # mid 보다 작거나 같은 값 몇 개인지 계산
    cnt = 0
    for i in range(1, n+1):
        cnt += min(mid//i, n)
    
    if cnt >= k:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)