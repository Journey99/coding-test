# 단어 정렬

n = int(input())
words = []

for i in range(n):
    word = str(input())
    cnt = len(word)
    words.append((word, cnt))

# 증복되는 단어 삭제
words = list(set(words))

# 단어를 길이순 - 알파벳 순으로 정렬
words.sort(key = lambda word: (word[1], word[0]))

for w in words:
    print(w[0])