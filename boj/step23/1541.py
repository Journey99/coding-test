# 잃어버린 괄호

expr = input()

# -를 기준으로 수식 나누기
parts = expr.split('-') 

# 첫번째 덩어리는 그대로 더하기
result = sum(map(int, parts[0].split('+')))

# 나머지는 괄호로 묶어서 뺌
for p in parts[1:]:
    result -= sum(map(int, p.split('+')))

print(result)
