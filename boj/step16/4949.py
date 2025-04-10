import sys

while True:
    sentence = input()

    if sentence == '.':
        break
    
    stack = []
    is_valid = True

    for s in sentence: 
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if stack:
                p = stack.pop()
                if p == '(':
                    pass
                else:
                    is_valid = False
                    break
            else:
                is_valid = False
                break
        elif s == ']':
            if stack:
                p = stack.pop()
                if p == '[':
                    pass
                else:
                    is_valid = False
                    break
            else:
                is_valid = False
                break
            
        
    if not stack and is_valid:
        print("yes")
    else:
        print("no")