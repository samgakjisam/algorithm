def dfs(i,j): # 시작할 점을 인자로 받음
    stack = []
    visited[i][j] = 1  # 첫 방문

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    while True:
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M and maze[ni][nj] == 1:
                if visited[ni][nj] == 0:  # 방문한 적 없으면
                    visited[ni][nj] = 1 # 방문 기록 남기고
                    stack.append([i,j])
                    # 다음 칸 = 이전 칸 + 1 (처리)
                    maze[ni][nj] = maze[i][j] + 1
                    i, j = ni, nj
                    break
        else:
            if stack:
                i, j = stack.pop()
            else:
                break

N, M = map(int, input().split())

maze = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)] # 방문 기록

dfs(0,0)

print(maze[N-1][M-1])



