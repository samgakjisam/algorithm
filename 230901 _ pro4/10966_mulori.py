'''
BFS 특징 : 출발지가 여러개
상하좌우 이동 가능
BFS 함수에서 상하좌우로 이동해서 물 칸으로 이동했을 때 최소 cnt
'''
def enque(item):
    global rear
    rear += 1
    Q[rear] = item

def deque():
    global front
    front += 1
    return Q[front]


def bfs(si,sj):
    enque([si,sj])
    visited = [[0] * M for _ in range(N)]
    visited[si][sj] = 1
    while front != rear:
        k,p = deque()
        if arr[k][p] == 'W':
            # if min_c > visited[k][p]:
            #     min_c = visited[k][p]
            return visited[k][p] -1
        for dk,dp in [0,1],[1,0],[0,-1],[-1,0]:
            # c += 1 # 다음 곳의 c
            nk,np = k+dk, p+dp
            if 0<=nk<N and 0<=np<M: # 범위 안 벗어나면
                if visited[nk][np]: # 이미 방문된 곳이면
                    if visited[nk][np] > visited[k][p] + 1:
                        visited[nk][np] = visited[k][p] + 1
                else:
                    enque([nk,np]) # 큐에 저장 (다음에 탐색할 곳)
                    visited[nk][np] = visited[k][p] + 1

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr =[list(map(str, input())) for _ in range(N)]
    Qsize = N*M
    Q = [0] * (Qsize * Qsize)
    rear = -1
    front = -1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'L':
                cnt += (bfs(i,j))

    print(f'#{tc} {cnt}')