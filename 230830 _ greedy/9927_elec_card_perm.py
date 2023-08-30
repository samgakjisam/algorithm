def perm(i,K): # N개 순서 정하기
    global min_v
    if i == K:
        s = 0
        s += arr[0][p[0]]
        s += arr[p[K-1]][0]
        for k in range(K-1):
            s += arr[p[k]][p[k+1]]
        if min_v > s:
            min_v = s
        return
    else:
        for j in range(K):
            if used[j] == 0:
                used[j] = 1
                p[i] = j+1 # 인덱스 맞추기
                perm(i+1,K)
                used[j] = 0

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    K = N - 1
    arr = [list(map(int, input().split())) for _ in range(N)]

    used = [0] * K
    p = [0] * K
    min_v = 1e9

    perm(0, K)

    print(f'#{tc} {min_v}')