# 도키도키 간식드리미

n = int(input())
numbers = list(map(int, input().split()))
stack = []
i = 1

for num in numbers:
    stack.append(num)

    while stack and stack[-1] == i:
        stack.pop()
        i += 1

if stack:
    print("Sad")
else:
    print("Nice")


