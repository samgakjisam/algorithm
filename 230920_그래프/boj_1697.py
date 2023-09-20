def bfs(s,e):
    visited = [-1] * (1000001)
    visited[s] = 0
    q = [s]
    while q:
        i = q.pop(0)
        if i == e:
            return visited[i]
        for k in [i+1, i-1, i*2]:
            if 0<=k<=100000 and visited[k] == -1:
                visited[k] = visited[i] + 1
                q.append(k)


N, K = map(int, input().split())

print(bfs(N,K))