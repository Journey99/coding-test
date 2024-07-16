# Z

n, r, c = map(int, input().split())
location = 0  # 몇사분면에 있는지
answer = 0

while n >= 1:
    temp = 2 ** (n - 1)

    if r < temp <= c:
        location = 2
    elif c < temp <= r:
        location = 3
    elif temp <= r and temp <= c:
        location = 4

    if n == 1:
        break
    answer += (location - 1) * (2 ** temp)
    if r > 1:
        r //= 2
    if c > 1:
        c //= 2
    n -= 1


if location == 2:
    answer += 1
elif location == 3:
    answer += 2
elif location == 4:
    answer += 3
print(answer)