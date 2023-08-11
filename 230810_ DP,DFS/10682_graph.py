def dfs(start, end, V, arr):
    visited = [0] * (V + 1)
    visited[start] = 1
    stack = []

    while True:
        for w in range(1, V + 1): # visited 끝 까지 / 오름차순으로
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
        return 1
    else:
        return 0

T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    arr = [[0] * (V + 1) for _ in range(V + 1)] # 1번부터 V번 까지

    for _ in range(E):
        v1, v2 = map(int, input().split())
        arr[v1][v2] = 1 # 핵심이다 ^^

    start, end = map(int, input().split())
    print(f'#{tc} {dfs(start, end, V, arr)}')

# 변수 설정을 잘하자
# 문제를 제대로 이해하기