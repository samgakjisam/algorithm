# # 이진 검색 - 반복문
#
# arr = [2,4,7,9,11,19,23]
#
# # 문제에서 데이터가 정렬되어 있다 라는 조건이 없다면
# # 반드시 정렬을 먼저 수행해야 한다.
# arr.sort()
#
# def binarySearch(target):
#     low = 0
#     high = len(arr) - 1
#
#     # low > high 라면 데이터를 못찾은 경우 중지
#     while low <= high:
#         mid = (low + high) // 2
#
#         # 1. 가운데 값이 정답인 경우
#         if arr[mid] == target:
#             return mid
#         # 2. 가운데 값이 정답보다 작은 경우
#         elif arr[mid] < target:
#             # 뒤 쪽으로 mid를 이동시킨다 (오른쪽에 답이 있다는 거니까)
#             low = mid + 1
#         # 3. 가운데 값이 정답보다 큰 경우 (왼쪽 검색)
#         else:
#             high = mid - 1
#
#
#     return "해당 데이터는 없습니다."
#
# print(f'9 = {binarySearch(9)}')
# print(f'4 = {binarySearch(4)}')
# print(f'19 = {binarySearch(10)}')

T = int(input())


def isbinarySearch(target):
    low = 0
    high = len(lst_1) - 1
    mid_count = 0
    left_count = 0
    right_count = 0
    stack = []
    is_not = True

    while low <= high:

        mid = (low + high) // 2

        if lst_1[mid] == target:

            mid_count += 1

            break

        elif lst_1[mid] < target:

            right_count += 1

            stack.append('R')

            if len(stack) >= 2 and stack[-1] == stack[-2]:
                is_not = False

            low = mid + 1

        else:

            left_count += 1

            stack.append('L')

            if len(stack) >= 2 and stack[-1] == stack[-2]:
                is_not = False

            high = mid - 1

    if is_not == False:
        return 0

    if mid_count == 1:

        if right_count == left_count or (right_count == 0 and left_count == 1) or (
                right_count == 1 and left_count == 0):
            return 1

    else:

        return 0


for tc in range(1, T + 1):

    N, M = map(int, input().split())

    lst_1 = list(map(int, input().split()))
    lst_1.sort()
    lst_2 = list(map(int, input().split()))
    cnt = 0

    for i in lst_2:

        if isbinarySearch(i):
            cnt += 1

    print(f"#{tc} {cnt}")