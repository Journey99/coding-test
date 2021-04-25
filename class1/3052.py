result = []
for i in range(10):
    num = int(input()) % 42
    if num not in result:
        result.append(num)

print(len(result))
