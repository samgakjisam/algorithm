T = int(input())

for tc in range(1, T + 1):

    N, S = map(int, input().split())

    arr = list(map(int, input().split()))

    cnt = 0

    for i in range(1, 1 << N):  # 원소가 N개인 집합의 부분집합의 개수 -> 공집합 제외 (1, 1<<N)
        subset = []
        for j in range(N):
            if i & (1 << j):  # 그 곳에 1이 있으면
                subset.append(arr[j])
        # 부분집합 나왔을 때 검증
        if sum(subset) == S:
            cnt += 1

    print(f'#{tc} {cnt}')