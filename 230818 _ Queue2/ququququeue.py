def bfs(s, V): # 시작정점 s, 마지막 정점 V
    visited = [0] * (V + 1)
    q = []
    q.append(s)
    visited[s] = 1
    # visited 생성
    # 큐 생성
    # 시작점 인큐
    # 시작점 방문표시
    while q: # 큐에 정점이 남아있으면 front != rear
        t = q.pop(0) # 디큐
        print(t) # 방문한 정점에서 할 일
        for w in adj_l[t]: # 인접한 정점 중 인큐되지 않은 정점 w가 있으면
            if visited[w] == 0:
                q.append(w)        # w 인큐, 인큐되었음을 표시(visited[t] + 1)
                visited[w] = visited[t] + 1


V, E = map(int, input().split())
arr = list(map(int, input().split()))

adj_l = [[] for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2 + 1]
    adj_l[v1].append(v2)
    adj_l[v2].append(v1) # 방향이 없는 경우
