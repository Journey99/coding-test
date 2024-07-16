# 1157

word = input().lower()
word_ls = list(set(word))

cnt = []
for i in word_ls:
    count = word.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(word_ls[cnt.index(max(cnt))].upper())


# 2941
word = input()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croatia:
    word = word.replace(i, "!")
print(len(word))


# 1316
n = int(input())
cnt = n
for i in range(n):
    word = input()
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            cnt -= 1
            break
print(cnt)


# 25206
grade_dict = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
sum_score = 0
s = 0
for i in range(20):
    subject_name, score, grade = input().split()
    if grade != 'P':
        s += float(score) * grade_dict[grade]
        sum_score += float(score)
print(s/sum_score)