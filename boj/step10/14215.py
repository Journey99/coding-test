# 세 막대

a, b, c = map(int, input().split())
lengths = sorted([a, b, c], reverse=True)

while lengths[0] >= lengths[1] + lengths[2]:
    lengths[0] -= 1
    lengths.sort(reverse=True)

print(sum(lengths))




