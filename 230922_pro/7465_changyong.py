'''
다 건너 건너 알 수 있으면 무리임
-> bfs로 할 수도 있음
-> 서로소 집합으로도 할 수 있음

BFS 풀이
=> 혼자있는 사람 생각해서 for문 돌려야 함
'''
# bfs
def bfs(s):
    q = []
    visited[s] = 1
    q.append(s)

    while q:
        k = q.pop(0)
        for w in G[k]:
            if visited[w] == 0:
                visited[w] = 1
                q.append(w)

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    G = [[] for _ in range(N+1)]
    for _ in range(M):
        f,t = map(int, input().split())
        G[f].append(t)
        G[t].append(f)

    visited = [0] * (N+1)
    cnt = 0 # 무리 개수

    for i in range(1, N + 1):
        if visited[i] == 0:
            cnt += 1
            if G[i]:
                bfs(i)

    print(f'#{tc} {cnt}')
