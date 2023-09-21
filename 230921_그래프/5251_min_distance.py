'''
일반통행 -> 단방향
0 -> N까지 최소 거리 -> 모든 곳을 들릴 필요가 없음 -> 다익스트라
크루스칼도 사용 가능? -> 굳이? 모든 정점이 이어지는 가중치의 최소값을 찾는 게 아님
'''
# 다익스트라
# 일단 최소 힙을 통해서 우선순위 큐를 만든다.
#

import heapq

def dijkstra(start):
    pq = [] # 힙
    # 출발점 초기화
    # pq 에 (0,start)를 넣는다 -> 앞 원소(누적거리)를 기준으로 우선순위를 설정한다.
    heapq.heappush(pq, (0,start))
    distance[start] = 0

    while pq:
        # 누적거리가 가장 작은 노드에 대한 정보를 pq에서 꺼냄
        d, now = heapq.heappop(pq) # 누적거리, 현재 노드 번호

        # 방문 여부 -> distance 배열은 1e9로 초기화 되어있음
        # + 기존에 기록된 누적 거리가 이미 최소 거리이면
        # -> 다음으로 (이 경로는 버림)
        if distance[now] < d:
            continue

        # 인접한 노드들을 확인한다.
        for next in graph[now]:
            # next = [다음노드 t, 다음노드까지의 거리 w]
            next_node = next[0]
            dist = next[1]

            # newx_node로 가기 위한 누적 거리
            new_dist = d + dist

            # next_node까지 가는 누적거리가 기존보다 더 크면
            # -> 다음으로
            if distance[next_node] < new_dist:
                continue

            # 아니면
            # 누적 거리 갱신하고 힙에 (누적거리, 노드 번호) 저장
            distance[next_node] = new_dist
            heapq.heappush(pq, (new_dist, next_node))





T = int(input())
for tc in range(1, T + 1):
    # 정점은 0 ~ N까지 있음
    N, E = map(int, input().split()) # 마지막, 도로의 개수
    # 인접리스트
    graph = [[] for _ in range(N+1)]
    for _ in range(E): # 경로 정보
        f,t,w = map(int, input().split())
        graph[f].append([t,w])

    # 누적 거리를 저장하는 배열 (최소를 구해야 함)
    INF = int(1e9)
    distance = [INF] * (N + 1)

    dijkstra(0) # 0이 시작
    print(f'#{tc} {distance[N]}')
