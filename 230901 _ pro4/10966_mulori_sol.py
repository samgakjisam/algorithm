'''
물에서부터 시작해서 찾는다.
시간 줄이기
1. deque 만들기
2.
'''
from collections import deque
def bfs(N,M):
    # 큐 생성
    q = deque()
    visited = [[-1] * M for _ in range(N)] # visited 생성 ************
    for i in range(N): # 시작점 인큐, 모든 물에서 시작
        for j in range(M):
            if arr[i][j] == 'W':
                q.append((i,j))
                visited[i][j] = 0 # 시작점(물) 표시 ***************
    while q: # 거리를 구할 칸이 남아 있으면 ...
        i, j = q.popleft()
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]: # i,j에 인접한 육지 찾기
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 'L' and visited[ni][nj] == -1:
                q.append((ni,nj))
                visited[ni][nj] = visited[i][j] + 1
    # 모든 육지에 대한 거리
    s = 0
    for i in range(N):
        for j in range(M):
            s += visited[i][j]
    return s

T = int(input())
for tc in range(1, T + 1):
    N,M = map(int, input().split())
    arr = [input() for _ in range(N)]
    print(f'#{tc} {bfs(N,M)}')