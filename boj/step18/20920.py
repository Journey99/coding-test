# 영단어 암기는 괴로워
import sys

n, m = map(int, input().split())
words = {}

for _ in range(n):
    word = sys.stdin.readline().strip()
    if len(word) < m:  # 단어 길이가 m보다 짧은 경우 저장 안함
        continue
    if word in words.keys():
        words[word] += 1
    else:
        words[word] = 1

words = sorted(words.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for word, _ in words:
    print(word)
        