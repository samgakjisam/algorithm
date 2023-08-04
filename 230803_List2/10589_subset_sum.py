T = int(input())
arr = [i for i in range(1, 13)]
n = len(arr)

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    cnt = 0
    for i in range(1 << n):  # 부분 집합의 개수
        subset = []
        for j in range(n):  # 원소의 수만큼 비트를 비교함
            if i & (1 << j):
                subset.append(arr[j])
        if sum(subset) == K and len(subset) == N: # N개의 부분집합 원소, 합 K
            cnt += 1

    print(f'#{tc} {cnt}')