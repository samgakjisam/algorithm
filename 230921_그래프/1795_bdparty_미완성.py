'''
단방향 간선
X번 집으로 모인다.

갔다 오는 최단 경로를 찾는다.
다익스트라

가는길 다익스트라 -> 그냥 그래프 출발 = X
돌아가는 길 다익스트라 -> 화살표 방향 바꾼 그래프 출발 = X

'''
import heapq
def dijk(s,e,g,d):
    pq = []
    # 초기화
    heapq.heappush(pq, (g[s][0], g[s][1]))
    d[s] = 0

    while pq:
        cost, now = heapq.heappop(pq)

        # 이미 입력되어있는 값이 현재노드까지의 거리보다 작다면 이미 방문한 노드이다.
        if g[now][1] < cost:
            continue

        new_cost = g[now]


T = int(input())
for tc in range(1, T + 1):
    N, M, X = map(int, input().split()) # M은 간선 수, X는 인수집
    graph = [[] for _ in range(N+1)]
    graph_2 = [[] for _ in range(N+1)] # 돌아갈 때

    for _ in range(M):
        x,y,c = map(int, input().split())
        graph[x].append((c,y)) # 우선순위 큐를 위해서

    INF = int(1e9)
    # 누적 거리
    dist = [INF] * (N+1) # 인수네 집으로 갈 때 비용
    dist_2 = [INF] * (N+1) # 인수네 집에서 자기 집으로 돌아갈 때 비용

    for i in range(1, N+1):
        if i == X: # 인수집이면
            continue
        dijk(X,i, graph,dist)
        dijk(X,i, graph_2,dist_2)


