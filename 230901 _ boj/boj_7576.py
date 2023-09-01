'''
대각선 안됨
토마토 다 익으려면 며칠이 걸리는지??
일부 칸에는 토마토 안들어있을 수도 있음
1은 익토, 0은 안익토, -1은 x토
bfs를 쓴다.
'''
from collections import deque

def bfs(st):
    q = deque()
    while st:
        q.append(st.popleft())
    temp = []
    t = 0
    while True: # 큐 없을 때 까지 반복
        i, j = q.popleft()
        good[i][j] = 1 # 익음 -> 방문기록
        for k in range(4): # 오아왼위
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<N and 0<=nj<M and good[ni][nj] == 0: # 벗어나지 않고 방문 x
                if tomato[ni][nj] == 0:
                    temp.append((ni,nj))
                # 이외에는 -1이나 1일 때
        # q 다 없애면 하루 지난 거임
        if not q:
            if temp:
                q = temp
                temp = []
                t += 1
            else:
                break

    # 다 했을 때 0 이 하나라도 있으면 -1
    # 그냥 해
    for i in range(N):
        for j in range(M):
            if good[i][j] == 0:
                return -1

    return t



M,N = map(int, input().split())

tomato = [list(map(int, input().split())) for _ in range(N)]

good = [[0] * M for _ in range(N)]

st = deque()

di = [0,1,0,-1]
dj = [1,0,-1,0]
xx = 0 # 안 익은거

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            st.append((i,j))
        if tomato[i][j] == -1:
            xx += 1
            good[i][j] = -1

ans = N*M - xx # 다 익어야 할 토마토

print(st)

# 이미 다 익었을 때
if len(st) + xx == M * N:
    print(0)
else:
    print(bfs(st))

