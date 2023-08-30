'''
인접한 배추에 벌레 이동 가능 -> 인접한 영역이 몇 개인지?
-> DFS 활용해서 더 이상 못가면 return 1해서 카운팅
'''

'''
import sys
sys.setrecursionlimit(10**6)
-> 재귀 횟수 설정

메모리 초과
-> pypy가 아니라 python으로 돌렸을 때는 통과
'''

import sys
sys.setrecursionlimit(10**6)

def dfs(i,j):
    visited[i][j] = 1
    di = [0,1,0,-1]
    dj = [1,0,-1,0]

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0<=ni<N and 0<=nj<M: # 범위를 안 벗어났을 때
            if visited[ni][nj] == 0 and baechu[ni][nj] == 1: # 갈 곳 있고, 간 적 없으면
                dfs(ni,nj)
    else: # 다 돌았는데 없으면
        return 1


T = int(input())

for tc in range(1, T + 1):
    M,N,K = map(int, input().split())# 가로, 세로, 배추 개수

    baechu = [[0] * M for _ in range(N)]

    for _ in range(K): # 배추 위치
        a,b = map(int, input().split())
        baechu[b][a] = 1

    visited = [[0] * M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and baechu[i][j] == 1:
                cnt += dfs(i,j)

    print(cnt)

