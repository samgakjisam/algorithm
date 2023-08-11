def dfs(start, end, arr):
    stack = []  # 스택 생성
    visited = [0] * (end + 1)  # end + 1 = 7
    visited[start] = 1  # [0, 1, 0, 0, 0, 0, 0]

    while True:
        for w in range(1, end + 1):  # visited 끝 까지 / 오름차순으로
            if arr[start][w] == 1 and visited[w] == 0:  # 출발지점에서 간선이 연결되있는 배열 1 and 도착지점 한 번도 안 들렸다면
                stack.append(start)  # stack에 start 넣기
                start = w  # 도착한 곳을 출발지점으로 지정
                visited[w] = 1  # 방문했다.
                break  # 탐색했으니까 for문 빠져나가서 다음 노드에서 for문 진행
            else:  # for문 안되면 (갈 곳이 없으면)
                if stack:  # 돌아갈 곳이 있니?
                    stack = stack.pop()  # 돌아가기
                else:  # 스택 비어있으면
                    break  # while문 탈출
    return


T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    arr = [[0] * (V + 1) for _ in range(V + 1)]  # 1번부터 V번 까지

    for _ in range(E):
        f, t = map(int, input().split())
        arr[start][end] = 1

    start, end = map(int, input().split())  # 1, 6
    dfs(start, end, arr)

