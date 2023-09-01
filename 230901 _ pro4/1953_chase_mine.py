def bfs(si, sj, L):
    q = []
    visited = [[0] * M for _ in range(N)]
    st = 1
    q.append([si, sj, st])
    while q:
        i, j, l = q.pop(0)  # 위치, 시간
        visited[i][j] = 1
        if l == L:  # 시간 다 됐으면
            pass
        else:
            for k in tu[info[i][j]]:
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < M and info[ni][nj] != 0 and visited[ni][nj] == 0:  # 안 벗어나고 가는 곳 0 아니면
                    # 돌아갈 수 있는 지 확인
                    if (k + 2) % 4 in tu[info[ni][nj]]:  # 돌아갈 수 있으면
                        q.append([ni, nj, l + 1])
    cnt = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 1:
                cnt += 1

    return cnt


T = int(input())

for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())

    info = [list(map(int, input().split())) for _ in range(N)]
    # 오아왼위
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    # 터널을 만났을 때 갈 수 있는 방향 (k)
    tu = [0, [0, 1, 2, 3], [1, 3], [0, 2], [0, 3], [0, 1], [1, 2], [2, 3]]

    print(f'#{tc} {bfs(R, C, L)}')