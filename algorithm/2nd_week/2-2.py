# 중복 문자 없는 가장 긴 부분 문자열 찾기

def longest_str(s):
    char_idx = {}
    start = 0
    max_len = 0

    for i, char in enumerate(s):
        if char in char_idx and char_idx[char] >= start:
            start = char_idx[char] + 1
        else: 
            max_len = max(max_len, i - start + 1)

        char_idx[char] = i
    
    return max_len

print(longest_str(input()))
