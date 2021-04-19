a = int(input())
b = int(input())
c = int(input())

result = str(a*b*c)  # a,b,c 값을 문자열에 저장
for i in range(10):
    print(result.count(str(i)))


