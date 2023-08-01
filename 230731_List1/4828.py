T = int(input()) # 테스트 케이스 개수
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_v = arr[0] # or 문제에서 나오는 가장 작은 수
    min_v = arr[0] # or 문제에서 나오는 가장 큰 수
    for i in range(1, N):
        if max_v < arr[i]:
            max_v = arr[i]
        if min_v > arr[i]:
            min_v = arr[i]
    ans = max_v - min_v
    print(f'#{tc} {ans}')