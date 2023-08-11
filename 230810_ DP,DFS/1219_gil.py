def dfs(start, end, V, arr):
    visited = [0] * (V + 1)
    visited[start] = 1
    stack = []
    can_99 = 0

    while True:
        for w in range(V): # 0 - 99
            if arr[start][w] == 1 and visited[w] == 0: # 출발지점에서 간선이 연결되있는 배열 1 and 도착지점 한 번도 안 들렸다면
                stack.append(start)
                start = w # 도착한 곳을 출발지점으로 지정
                visited[start] = 1 # 방문했다.
                break # 탐색했으니까 for문 빠져나가서 다음 노드에서 for문 진행
        else:
            if stack:# 스택에 지나온 정점이 남아있으면
                start = stack.pop() # pop()해서 다시 다른 w를 찾을 n 준비
            else:       # 스택이 비어있으면
                break       # while True 탐색 끝
        if visited[end] == 1:
            can_99 = 1
            break
    if can_99 == 1:
        return 1
    return 0


T = 10

for tc in range(1, T + 1):
    test_case, length = map(int, input().split())
    arr = list(map(int, input().split()))

    gil = [[0] * 100 for _ in range(100)]

    for i in range(length * 2):
        if i % 2 == 0:
            gil[arr[i]][arr[i + 1]] = 1

    start = 0
    end = 99
    print(f'#{tc} {dfs(start, end, 100, gil)}')
