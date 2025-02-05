# 진법 변환2
## 10진법 수 N을 B진법으로 변환

n, b = map(int, input().split())
ary = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ''

while n > 0:
    rem = n % b  # 현재 자리의 나머지
    result += ary[rem]  # 나머지를 변환된 문자로 추가
    n //= b  # 몫을 갱신하여 다음 자리 계산

result = result[::-1]
print(result)
