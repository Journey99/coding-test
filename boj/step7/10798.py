# 세로 읽기

words = []
length = []

for _ in range(5):
    word = input()
    words.append(word)
    length.append(len(word))

result = ''
for i in range(max(length)):
    for j in range(5):
        if length[j] > i:
            result += words[j][i]
            
print(result)