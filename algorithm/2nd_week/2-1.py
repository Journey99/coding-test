# 후위 표기법 계산하기

def calc_postfix(text):

    tokens = text.split()
    s = []

    for token in tokens:
        if token.isnumeric():
            s.append(int(token))
        elif token in ['+', '-', '*', '/']:
            n2 = s.pop()
            n1 = s.pop()
            
            if token == "+":
                s.append(n1 + n2)
            elif token == '-':
                s.append(n1 - n2)
            elif token == '*':
                s.append(n1 * n2)
            else:
                if n2 == 0:
                    raise ZeroDivisionError
                s.append(n1 // n2)
        else:
            raise ValueError(f"유효하지 않은 값 : {token}")

    return s[0]

text = input()
print(calc_postfix(text))