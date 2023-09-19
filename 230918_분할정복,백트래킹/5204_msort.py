def merge(left, right):
    result = []
    global cnt
    if left[-1] > right[-1]:
        cnt += 1
    # 한 쪽이 빌 때까지 반복
    while len(left) > 0 or len(right) > 0:
        # 둘 다 남아 있으면, 두 리스트의 가장 앞에 있는 것 중 작은 것을 선택하여 result 에 추가
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        # 한 쪽만 남아있으면, 남은것을 모두 result 에 추가
        elif len(left) > 0:
            result.append(left.pop(0))
        elif len(right) > 0:
            result.append(right.pop(0))

    return result

def merge_sort(unordered_list):
    # 길이가 1인 배열까지 나누면 stop
    if len(unordered_list) == 1:
        return unordered_list

    left = []
    right = []
    middle = len(unordered_list) // 2
    # 왼쪽을 따로 리스트에 저장
    for el in unordered_list[:middle]:
        left.append(el)

    # 오른쪽을 따로 리스트에 저장
    for el in unordered_list[middle:]:
        right.append(el)

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    merge_sort(arr)  # 인덱스를 넘겨주기기
    print(f'#{tc} {arr[N // 2]} {cnt}')

# def merge_sort(unordered_list):
#     # 길이가 1인 배열까지 나누면 stop
#     if len(unordered_list) == 1:
#         return unordered_list
#
#
#     middle = len(unordered_list) // 2
#     # 왼쪽을 따로 리스트에 저장
#     left = unordered_list[:middle]
#     # 오른쪽을 따로 리스트에 저장
#     right = unordered_list[middle:]
#
#     left = merge_sort(left)
#     right = merge_sort(right)
#
#     return merge(left, right)
