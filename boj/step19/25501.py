# 재귀의 귀재

def recursion(s, l, r):
    global cnt
    cnt += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

t = int(input())
for _ in range(t):
    cnt = 0
    string = input()
    result = isPalindrome(string)
    print(f'{result} {cnt}')