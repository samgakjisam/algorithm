# 가중치의 합이 최소가 되도록 함
# 1. prim -> 최소 힙 -> 최소부터 찾아가며 방문하지 않은 노드가 연결된 간선 선택
# 2. kruskal -> 가중치 기준 오름차순 sort -> 서로소 집합으로 사이클 발생 여부 확인


'''
최소신장트리를 구성하는 간선의 가충치를 모두 더해 출력
'''
T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split()) # 마지막 노드번호, 간선의 개수
    # f, t, w 입력을 받는다. -> 인접 행렬
    graph = []

    # 그래프 정보 입력
    for _ in range(E):
        f,t,w = map(int, input().split())
        graph.append([f,t,w])

    # w를 기준으로 오름차순 정렬한다.
    graph.sort(key= lambda x: x[2])

    # 사이클 여부 확인을 위해서 union find를 해야함 -> 부모 정보(처음은 그냥 자신이 부모)
    parents = [i for i in range(V+1)] ## V는 마지막 노드의 번호임

    # find_set -> 부모 확인
    def find_set(x):
        if parents[x] == x: # 부모가 자기 자신이면
            return x

        else:
            # 경로 압축 -> 부모의 부모가 있으면 그 정보를 갱신하면서 찾는다.
            # 부모의 부모를 찾아서 그 값을 갱신
            parents[x] = find_set(parents[x])
            return parents[x]

    # 트리 구성
    def union(x,y):
        # 우선 부모 정보 갱신
        x = find_set(x)
        y = find_set(y)

        if x == y: # 사이클이 발생함
            return

        if x < y: # 최소를 부모(루트)로
            parents[y] = x
        else:
            parents[x] = y

    # 방문한 정점의 수
    cnt = 0
    # 간선의 가중치 합
    s = 0

    # 그래프를 순회하면서 최소값이 부모인 서로소 집합만들기
    for f,t,w in graph:
        # 싸이클 발생 여부 확인
        if find_set(f) != find_set(t):
            cnt += 1
            s += w
            union(f,t)
            # MST 구성이 끝남 -> 모든 정점을 방문함
            if cnt == V:
                break

    print(f'#{tc} {s}')


