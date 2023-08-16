def dfs(i, j, maze):
    stack = [] # 스택
    while True:
        for [di,dj] in [[0,1],[1,0],[0,-1],[-1,0]]: # 오아왼위
            ni = i + di
            nj = j + dj
            if maze[ni][nj] != 1 and 0 <= ni < N and 0 <= ni < N and 0 <= nj < N: # 가는 곳이 통로이고 벗어나지 않으면
                stack.append((i,j)) # 돌아갈 길
                i = ni
                j = nj # 출발지 변경
                if stack[ni][nj] == 3:
                    return 1
                break
            else: # 다 돌았는데 갈 길 없음
                if stack:
                    i,j = stack.pop()
                else:
                    return 0




def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j
    # return -1, -1 # 없을 경우

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    # 찾는 방법 최적화
    # 경로 설정
    sti, stj = find_start(N)
    dfs(sti, stj, maze)