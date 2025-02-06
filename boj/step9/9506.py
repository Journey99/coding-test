# 약수들의 합
## 자신을 제외한 모든 약수들의 합이 자기자신과 같은 수를 완전수
## n이 완전수인지 아닌지 판단해주는 프로그램 출력

while True:
    n = int(input())
    if n == -1:
        break

    divisors = []
    for i in range(1, n//2 + 1):
        if n % i == 0:
            divisors.append(i)
    
    if sum(divisors) == n:
        print(n, "=", " + ".join(str(x) for x in divisors))

    else:
        print(f"{n} is NOT perfect.")