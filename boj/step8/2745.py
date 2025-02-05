# 진법 변환
## B진법 수 N을 10진법으로 바꿔 출력하기
n, b = input().split()
print(int(n, b))

## 진법변환 원리 적용
ary = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = n[::-1]
result = 0
for i, n in enumerate(n):
    result += (int(b)**i) * (ary.index(n))
print(result)