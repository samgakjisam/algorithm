'''
연결요소란 하나여도 되고 이어져 있으면 된다.
'''

'''
재귀가 더 느릴지도
'''
import sys
sys.setrecursionlimit(10**6)

def dfs(s):
    visited[s] = 1
    for i in range(1, N + 1):
        if info[s][i] == 1: # 길 있고
            if visited[i] == 0:
                dfs(i) # 다 갔다왔는데
    else:
        return


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