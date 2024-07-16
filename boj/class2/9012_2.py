# 괄호

n = int(input())

def check(brackets):
    stack = []

    for i in brackets:
        if i =='(':
            stack.append(i)
        else:
            if not stack:
                print("NO")
                return
            else:
                stack.pop()

    if not stack:
        print("YES")
        return
    else:
        print("NO")

for _ in range(n):
    brackets = input()
    check(brackets)