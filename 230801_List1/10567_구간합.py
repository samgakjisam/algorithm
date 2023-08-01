T = int(input())

for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    summation = 0
    max_summation = 0
    min_summation = 1e10

    for i in range(len(arr) - M + 1):
        summation = 0
        for j in range(M):
            summation += arr[i + j]
        if min_summation > summation:
            min_summation = summation
        if max_summation < summation:
            max_summation = summation

    ans = max_summation - min_summation

    print(f'#{tc} {ans}')