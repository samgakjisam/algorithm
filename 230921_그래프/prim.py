'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

'''
MST 방문 순서 디버깅으로 확인
prim 알고리즘
'''

import heapq
# 우선순위 큐를 위해서
# 튜플은 맨 앞의 데이터를 기준으로 정렬한다.

def prim(start):
    heap = []
    sum_weight = 0
    # MST에 포함되었는지 여부
    MST = [0] * V

    # 가중치, 정점 정보
    heapq.heappush(heap, (0, start))

    while heap:
        # 가장 적은 가중치를 가진 정점을 꺼냄
        weight, v = heapq.heappop(heap)

        # 이미 방문한 노드라면 pass
        if MST[v]:
            continue

        # 방문 체크
        MST[v] = 1

        # 누적합 추가
        sum_weight += weight

        for next in range(V):
            # 갈 수 없거나 이미 방문했다면 pass
            if graph[v][next] == 0 or MST[next]:
                continue

            heapq.heappush(heap, (graph[v][next], next))

    return sum_weight

    # heapq.heappush(heap, (-3, 2))
    # heapq.heappush(heap, (-1, 1))
    # heapq.heappush(heap, (-2, 3))
    #
    # print(heapq.heappop(heap))
    # print(heapq.heappop(heap))
    # print(heapq.heappop(heap))


V, E = map(int, input().split())
# 인접행렬
graph = [[0] * V for _ in range(V)]

for _ in range(E):
    f, t, w = map(int, input().split())
    # 실수하면 안되는거 -> 양방향인지 단방향인지 확인
    graph[f][t] = w
    graph[t][f] = w

result = prim(0)
print(f'최소 비용 = {result}')
