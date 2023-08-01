# 11092 최대 최소 간격
T = int(input()) # 테스트 케이스 개수

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    min_idx = 0
    max_idx = 0

    for i in range(1, N):
        if arr[min_idx] > arr[i]: # 최소값 인덱스는 가장 왼쪽
            min_idx = i
        if arr[max_idx] <= arr[i]:  # 최대값 인덱스는 가장 오른쪽
            max_idx = i

    ans = abs(max_idx - min_idx) # 간격
    print(f'#{tc} {ans}')

# 11092 최대 최소 간격
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    min_idx = 0
    max_idx = 0

    for i in range(1, N):
        if arr[min_idx] > arr[i]:
            min_idx = i
        if arr[max_idx] <= arr[i]:
            max_idx = i

    ans = abs(max_idx - min_idx)
    print(f'#{tc} {ans}')


# 10565 minmax 제출용
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#
#     min_idx = 0
#     max_idx = 0
#
#     for i in range(1, N):
#         if arr[min_idx] > arr[i]:
#             min_idx = i
#         if arr[max_idx] <= arr[i]:
#             max_idx = i
#
#     ans = arr[max_idx] - arr[min_idx]
#     print(f'#{tc} {ans}')