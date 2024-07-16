n, m = map(int, input().split())
tree = list(map(int, input().split()))
start = 1
end = max(tree)           # 이분탐색 검색 범위 설정

while start <= end:
    mid = (start+end) // 2

    log = 0 # 벌목된 나무의 총합
    for i in tree:
        if i >= mid:
            log += i - mid
    # 벌목 높이 이분탐색
    if log >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)

