# 알고리즘 수업 - 병합 정렬 1

save_count = 0
kth_value = -1  

def merge_sort(a, k):
    if len(a) <= 1:
        return a

    mid = len(a) // 2
    left = merge_sort(a[:mid], k)
    right = merge_sort(a[mid:], k)
    return merge(left, right, k)

def merge(left, right, k):
    global save_count, kth_value
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            save_count += 1
            if save_count == k:
                kth_value = left[i]
            i += 1
        else:
            result.append(right[j])
            save_count += 1
            if save_count == k:
                kth_value = right[j]
            j += 1

    while i < len(left):
        result.append(left[i])
        save_count += 1
        if save_count == k:
            kth_value = left[i]
        i += 1

    while j < len(right):
        result.append(right[j])
        save_count += 1
        if save_count == k:
            kth_value = right[j]
        j += 1

    return result

n, k = map(int, input().split())
a = list(map(int, input().split()))

merge_sort(a, k)
print(kth_value)