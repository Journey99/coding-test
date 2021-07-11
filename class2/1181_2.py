# 단어 정렬

n = int(input())

# 1. 단어를 입력받음
words = []
for i in range(n):
    words.append(input())

# 2. 중복되는 단어를 삭제
# 중복을 허용하지 않는 set
set_words = list(set(words))

# 3. 길이와 단어 쌍으로 묶어서 저장
sort_words = []
for i in set_words:
    sort_words.append((len(i), i))

# 4. 단어 정렬
result = sorted(sort_words)

for len_word, word in result:
    print(word)
