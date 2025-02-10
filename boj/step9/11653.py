# 소인수분해

n = int(input())
result = []

if n >= 2:
    for i in range(2, n+1):
        while True:
            if n % i == 0 and n > 1:
                result.append(i)
                n = n // i
            else:
                break
    print('\n'.join(map(str, result)))       
