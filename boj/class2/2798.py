N, M = map(int, input().split())
card = list(map(int, input().split()))
sum = []

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            ssum = card[i] + card[j] + card[k]
            if ssum <= M :
                sum.append(ssum)


print(max(sum))
