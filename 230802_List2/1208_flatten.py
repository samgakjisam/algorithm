T = 10
for tc in range(1, T + 1):
    can_dump = int(input())
    arr = list(map(int, input().split()))
    max_idx = 0
    min_idx = 0

    for i in range(1, can_dump + 1):
        for m in range(100):
            if arr[max_idx] <= arr[m]:
                max_idx = m
            if arr[min_idx] >= arr[m]:
                min_idx = m
        arr[max_idx] -= 1
        arr[min_idx] += 1
    for m in range(100):
        if arr[max_idx] <= arr[m]:
            max_idx = m
        if arr[min_idx] >= arr[m]:
            min_idx = m

    ans = arr[max_idx] - arr[min_idx]
    print(f'#{tc} {ans}')
