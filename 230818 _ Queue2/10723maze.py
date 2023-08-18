def bfs(sti, stj, N):
    # visited
    # 큐
    # 시작점 인큐
    # 시작점 방문표시
    visited = [[0] * N for _ in range(N)]
    q = []
    q.append((sti, stj))
    visited[sti][stj] = 1
    while q: # 방문할 곳이 있니? # 큐가 비워질 때 까지
        i, j = q.pop(0) # 디큐
        # 처리
        if maze[i][j] == 3: # 도착
            return visited[i][j] - 2 # 도착, 시작점 거리를 뺀 지나온 칸 수 리턴
        # 인접하고 인큐된 적이 없으면 # 인큐, 인큐표시
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni,nj = i + di, j + dj
            # 범위 안벗어나고 갈 곳이 벽이 아니고 방문한 적이 없으면
            if 0<=ni<N and 0<=nj<N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1


    return 0 # 모든 곳을 봤는데 3인 칸을 못찾음(3인 칸에 도달할 수 없는 경우)


def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    sti, stj = find_start(N) # 미로의 시작점 찾기

    ans = bfs(sti, stj, N) # 미로의 크기

    print(f'#{tc} {ans}')