n = int(input())
seq = []
op = []
count = 1
temp = True
for i in range(n):
    num = int(input())
    while count <= num:
        seq.append(count)
        op.append('+')
        count += 1
    if seq[-1] == num:
        seq.pop()
        op.append('-')
    else:
        temp = False
if temp == False:
    print("NO")
else:
    for i in op:
        print(i)



