# 길찾기(길이 있는지 없는지 1,0)
def bfs(sti, stj, maze):
    # 방문기록, 큐
    q = []
    q.append((sti,stj)) # 인큐
    visited = [[0] * 16 for _ in range(16)]
    visited[sti][stj] = 1 # 시작점 방문기록

    while q: # 큐 빌 때까지
        i, j = q.pop(0) # 디큐하고 그거를 시작점으로
        if maze[i][j] == 3: # 도착점이면
            return 1

        for di,dj in [[1,0],[0,1],[-1,0],[0,-1]]:
            ni = i + di
            nj = j + dj
            # 가려는 곳이 배열을 벗어나지 않고 벽이 아니고 방문하지 않았으면
            if 0<=ni<16 and 0<=nj<16 and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append((ni,nj)) # 인큐하고
                visited[ni][nj] = 1 # 방문기록

    return 0 # 다했는데 못찾았으면

# 시작점 찾기
def find_st(maze):
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                return i, j

T = 10

for tc in range(1, T + 1):
    test_case = int(input())
    maze = [list(map(int, input())) for _ in range(16)]

    sti, stj = find_st(maze)

    print(f'#{tc} {bfs(sti, stj, maze)}')