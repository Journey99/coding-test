# 2675
t = int(input())
for _ in range(t):
    r, string = input().split()
    for s in string:
        print(s*int(r), end='')
    print()


# 1152
s = input()
print(len(s.split()))


# 2908
a, b = input().split()
f_a, f_b = a[::-1], b[::-1]
print(max(int(f_a), int(f_b)))


# 5622
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
string = input()
time = 0
for s in string:
    for idx, i in enumerate(dial):
        if s in i:
            time += (idx + 3)
print(time)


# 11718
while True :
    try :
        print(input())
    except EOFError:
        break