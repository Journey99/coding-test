# 단어 정렬
import sys

n = int(input())
words = []

for _ in range(n):
    words.append(sys.stdin.readline().strip())

words_set = set(words) # 중복 제거
words_ls = list(words_set)
words_ls.sort() # 알파벳순으로 정렬
words_ls.sort(key=len) # 알파벳순으로 정렬된 상태를 유지하며 길이를 기준으로 정렬

for word in words_ls:
    print(word)