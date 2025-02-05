# 세탁소 사장 동혁
## 쿼터(Quarter, $0.25), 다임(Dime, $0.10), 니켈(Nickel, $0.05), 페니(Penny, $0.01)

t = int(input())
for _ in range(t):
    money = int(input())
    for i in [25, 10, 5, 1]:
        print(money//i, end=' ')
        money = money % i