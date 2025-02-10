# 네 번째 점
def find_unique(n1, n2, n3):
    if n1 == n2:  
        return n3
    elif n1 == n3:  
        return n2
    else:  
        return n1
    
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

print(find_unique(x1, x2, x3), find_unique(y1, y2, y3))


## 리스트 카운트 사용해서
x_nums = []
y_nums = []
for _ in range(3):
    x, y = map(int, input().split())
    x_nums.append(x)
    y_nums.append(y)

for i in range(3):
    if x_nums.count(x_nums[i]) == 1:
        x4 = x_nums[i]
    if y_nums.count(y_nums[i]) == 1:
        y4 = y_nums[i]
print(x4, y4)


## 첫번재 코드가 시간이 더 짧음 (4ms)