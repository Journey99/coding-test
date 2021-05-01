S = str(input())
alpabet = [chr(i) for i in range(97,122+1)]
# a부터 z까지

for i in alpabet:
    try:
        print(S.index(i), end=' ')
    except:
        print(-1, end=' ')