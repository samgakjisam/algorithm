'''
다리의 길이는 2 이상

모든 구역이 연결되어 있어야 한다.
'''
def bfs(si,sj, cnt):
    q = []
    visited[si][sj] = cnt
    q.append((si,sj))
    while q:
        i,j = q.pop(0)
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                if visited[ni][nj] == 0:
                    if mmap[ni][nj] == 1:
                        visited[ni][nj] = cnt
                        q.append((ni,nj))





N,M = map(int, input().split()) # 세로 i, 가로 j

mmap = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

di = [0,1,0,-1]
dj = [1,0,-1,0]

cnt = 0 # 섬의 개수 정보

# 섬 번호 붙이기
for i in range(N):
    for j in range(M):
        if mmap[i][j] == 1 and visited[i][j] == 0:
            cnt += 1
            bfs(i,j,cnt)


# 다리 연결해보기 + 연결관계 확인하기
dis = [[0] * (cnt+1) for _ in range(cnt+1)] # 두 섬 사이의 최단 거리, 단 2 이상인 경우만
