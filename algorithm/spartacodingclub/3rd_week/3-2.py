# 순열 생성하기
def generate_permutations(nums):
    def backtrack(path):
        if len(path) == len(nums):
            result.append(path[:])
            return
        for num in nums:
            if num not in path: 
                path.append(num)
                backtrack(path)
                path.pop()  

    result = []
    backtrack([])  
    return result

nums = eval(input())

permutations = generate_permutations(nums)
for perm in permutations:
    print(perm)
