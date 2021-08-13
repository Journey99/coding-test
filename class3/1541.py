# 잃어버린 괄호

import sys
input = sys.stdin.readline

order = input().rstrip()
sub1 = list(order.rsplit('-'))

temp = 0
first = True
for row in sub1:
    sub2 = list(map(int, ''.join(row).rsplit('+')))

    if first:
        first = False
        temp = sum(sub2)
    else:
        temp -= sum(sub2)

print(temp)