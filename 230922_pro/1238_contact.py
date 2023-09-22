'''
가장 나중에 연락을 받게 되는 사람 중 번호가 가장 큰 사람
연락이 퍼지기 때문에 BFS -> cnt 증가시키기
'''
def bfs(s,c):
    q = []
    q.append(s)
    visited[s] = c # 처음 -> 0

    while q:
        i = q.pop(0)
        for next in G[i]:
            if visited[next] == -1:
                visited[next] = (visited[i] + 1)
                q.append(next)

    return visited[i]


T = 10
for tc in range(1, T + 1):
    N, S = map(int, input().split())
    G = [[] for _ in range(101)] # 100명
    info = list(map(int, input().split()))
    for i in range(0,N,2):
        f,t = info[i], info[i+1]
        G[f].append(t)
    visited = [-1] * 101
    cnt = 0

    m = bfs(S,cnt)
    for i in range(100,-1,-1):
        if visited[i] == m:
            print(f'#{tc} {i}')
            break