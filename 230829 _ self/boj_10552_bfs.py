from collections import deque
import sys

def bfs(s):
    # 큐에 처음꺼 넣기
    q = deque() # 큐 만들기
    q.append(s) # 큐에 넣기
    cnt = 0
    while q: # 큐 없어질 때까지
        t = q.popleft()
        for j in info:
            if j[0] == t: # 간선 연결 되어 있으면
                if visited[j[1]] == 0: # 방문 한 적 없으면
                    q.append(j[1]) # 큐에 넣기
                    visited[j[1]] = 1
                    cnt += 1
                    break
                if visited[j[1]] == 1:
                    return -1
    return cnt



N,M,P = map(int, sys.stdin.readline().split())

info = [0] * N

for i in range(N):
    lik, hat = map(int, sys.stdin.readline().split())
    info[i] = [hat, lik]

visited = [0] * (M + 1)

print(bfs(P)) # P부터 시작