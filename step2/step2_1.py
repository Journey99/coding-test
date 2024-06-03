# 1330

a, b = map(int, input().split())

if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print("==")


# 9498
score = int(input())

if 90<= score <= 100:
    print("A")
elif 80 <= score <= 89:
    print("B")
elif 70 <= score <= 79:
    print("C")
elif 60 <= score <= 69:
    print("D") 
else:
    print("F")       


# 2753
y = int(input())

if y % 4 == 0 and y % 100 != 0:
    print(1)
elif y % 400 == 0:
    print(1)
else:
    print(0)
