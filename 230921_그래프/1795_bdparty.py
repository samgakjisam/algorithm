'''
단방향 간선
X번 집으로 모인다.

갔다 오는 최단 경로를 찾는다.
다익스트라

가는길 다익스트라 -> 그냥 그래프 출발 = X
돌아가는 길 다익스트라 -> 화살표 방향 바꾼 그래프 출발 = X

다익스트라 알고리즘
1. 시작점 초기화
2. 현재위치 꺼내기
3. 이미 입력되어 있는 현재까지의 누적합(처음이면 INF)보다 cost가 작다면 이미 방문한 노드이다.
4. 갈 수 있는 곳을 순회한다.
5. 갱신할 준비를 한다 (코스트)
6. 갈 곳의 누적합이 지금 갱신하려고 준비한 거보다 작은지 확인
7. 아니면은 힙에다 넣어줌
'''
import heapq
def dijk(s,g,di):
    pq = []
    # 초기화
    heapq.heappush(pq, (0, s))
    di[s] = 0
    while pq:
        # 현재 위치
        cost, now = heapq.heappop(pq)

        # 이미 입력되어있는 값이 현재노드까지의 거리보다 작다면 이미 방문한 노드이다.
        if di[now] < cost:
            continue
        # 갈 수 있는 곳 보기
        for n in g[now]:
            next_node = n[1]
            next_cost = n[0]
            # 누적합 + 현재 코스트 -> 갱신할 준비
            new_cost = cost + next_cost
            # 갈 곳의 누적합이 더 적다?
            if di[next_node] <= new_cost:
                continue
            # 아니라면 힙에다가 넣어주고 누적합 갱신
            di[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))


T = int(input())
for tc in range(1, T + 1):
    N, M, X = map(int, input().split()) # M은 간선 수, X는 인수집
    graph = [[] for _ in range(N+1)]
    graph_2 = [[] for _ in range(N+1)] # 돌아갈 때

    for _ in range(M):
        x,y,c = map(int, input().split())
        graph[x].append([c,y]) # 우선순위 큐를 위해서
        graph_2[y].append([c,x]) # 우선순위 큐를 위해서

    INF = int(1e9)
    # 누적 거리
    dist = [INF] * (N+1) # 인수네 집으로 갈 때 비용
    dist_2 = [INF] * (N+1) # 인수네 집에서 자기 집으로 돌아갈 때 비용
    # X에서 출발해서 모든 정점을 가는 최소 누적합
    dijk(X, graph,dist)
    dijk(X, graph_2,dist_2)

    max_v = 0
    for i in range(1, N+1):
        a = dist[i] + dist_2[i]
        if max_v < a:
            max_v = a
    print(f'#{tc} {max_v}')
