# 괄호
import sys

t = int(input())
for _ in range(t):
    stack = []
    ps = sys.stdin.readline().strip()
    is_valid = True

    for p in ps:
        if p == '(':
            stack.append(p)
        else:
            if stack:
                stack.pop()
            else:
                is_valid = False
                break 
    
    if is_valid and not stack:
        print("YES")
    else:
        print("NO")