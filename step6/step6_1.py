# 25083
print("         ,r\'\"7")
print("r`-_   ,\'  ,/")
print(" \\. \". L_r\'")
print("   `~\\/")
print("      |")
print("      |")


# 3003
a, b, c, d, e, f = map(int, input().split())
piece = [1, 1, 2, 2, 2, 8]
print(piece[0]-a, piece[1]-b, piece[2]-c, piece[3]-d, piece[4]-e, piece[5]-f)


# 2444
n = int(input())
for i in range(1, n):
    print(' '*(n-i) + '*'*(2*i-1))
for i in range(n, 0, -1):
    print(' '*(n-i) + '*'*(2*i-1))


# 10988
s = input()
r_s = s[::-1]
if s == r_s:
    print(1)
else:
    print(0)
