import sys

def dfs(s):
    visited[s] = 1
    stack = []
    while True:
        for w in range(1, N + 1):
            if visited[w] == 0 and info[s][w] == 1:
                stack.append(s)
                visited[w] = 1
                s = w
                break
        else:
            if stack:
                s = stack.pop()
            else:
                break


N,M = map(int, input().split()) # 정점, 간선

info = [[0] * (N+1) for _ in range(N+1)] # 0은 빼고

# 같은 간선은 한 번만 주어진다.
for _ in range(M):
    f, t = map(int, sys.stdin.readline().split())
    info[f][t] = 1
    info[t][f] = 1

visited = [0] * (N+1)
cnt = 0

for i in range(1,N+1):
    if visited[i] == 0:
        dfs(i)
        cnt += 1
        # i부터 출발해보자
print(cnt)