n = int(input())

for i in range(n):
    total = 0
    score = 0
    for j in input():
        if j == "O":
            score += 1
            total += score
        else:
            score = 0
    print(total)