def bfs(S,G,arr,V):
    # 방문기록
    # 큐
    # 시작점 방문 기록
    visited = [0] * (V + 1)
    q = []
    q.append(S)
    visited[S] = 1

    while q: # 큐 비어있을 때 까지
        # 디큐
        s = q.pop(0)
        # 인큐 + 방문기록
        for w in range(1, V + 1): # 간선 정보 보기 -------> 1부터하면되잖아
            # G 방문했을 때
            if visited[G]:
                return visited[G] - 1 # 출발지점 1 빼기

            # 갈 곳이 있을 때 + 방문한적이 없으면
            if arr[s][w] == 1 and visited[w] == 0:
                # 인큐 + 방문기록
                q.append(w)
                visited[w] = visited[s] + 1

    return 0 # 서로 연결 되어 있지 않다면면



T =int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())

    arr = [[0] * (V + 1) for _ in range(V + 1)]

    for i in range(E):
        f, t = map(int, input().split())
        # 방향성 없음
        arr[f][t] = 1
        arr[t][f] = 1

    S, G = map(int, input().split())
    print(f'#{tc} {bfs(S, G, arr, V)}') # 출발, 도착, 간선 정보, 노드 개수