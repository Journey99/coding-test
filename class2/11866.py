# 요세푸스 순열

n, k = map(int,input().split())
nums = [i for i in range(1, n+1)]
answer = []
tmp = 0
while len(answer) != n:
    tmp = (tmp + (k-1)) % len(nums)
    answer.append(nums.pop(tmp))

print("<%s>" %(", ".join(map(str,answer))))

# answer는 list이고 정수형이 들어있기 때문에 형변환