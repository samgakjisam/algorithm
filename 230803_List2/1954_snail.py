T = int(input())

for tc in range(1, T + 1):
    N = int(input()) # N x N
    arr = [[0] * N for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    i, j = 0, 0
    d = 0
    for k in range(1, (N ** 2 + 1)):  # 1 ~ 마지막
        arr[i][j] = k
        if (i + di[d] == -1 or i + di[d] == N or
            j + dj[d] == -1 or j + dj[d] == N or
            arr[i + di[d]][j + dj[d]] != 0): # 배열을 벗어나거나 앞에 뭐가 있음
                d = (d + 1) % 4
        i, j = i + di[d], j + dj[d]

    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(f'{arr[i][j]} ', end='')
        print()