word = input()
word = word.upper()  # 문자열을 대문자로 변경

# 알파벳 개수 세기
dic = {}
for i in word:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

# 가장 많이 사용된 알파벳 찾기
max_key = max(dic, key=dic.get)       # key를 기준으로 최대값을 찾는다.
max_value = dic[max_key]
dic.pop(max_key)                # max_key위치에 있는 요소를 pop
if max_value in dic.values():
    print("?")
else: print(max_key)