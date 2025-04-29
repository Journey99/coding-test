# 칸토어 집합

def cantor(start, length):
    if length == 1:
        return
    third = length // 3

    # 가운데 공백으로
    for i in range(start+third, start+2*third):
        line[i] = ' '
    
    cantor(start, third)
    cantor(start+2*third, third)


while True:
    try:
        N = int(input())
        length = 3 ** N  
        line = ['-'] * length  
        cantor(0, length)  
        print(''.join(line))  
    except EOFError:
        break