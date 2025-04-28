# 인사성 밝은 곰곰이
import sys

n = int(input())
emoji = set()
result = 0

for _ in range(n):
    string = sys.stdin.readline().strip()
    if string == 'ENTER':
        result += len(emoji)
        emoji.clear()     
    else:
        emoji.add(string)

result += len(emoji)
print(result)