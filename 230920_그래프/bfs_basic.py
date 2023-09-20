graph = [
    [0,1,0,1,0],
    [1,0,1,1,1],
    [0,1,0,0,0],
    [1,1,0,0,1],
    [0,1,0,1,0]
]

def bfs(start):
    visited = [0] * 5

    # 먼저 방문 했던 것을 먼저 처리해야 한다. = queue
    queue = [start]
    visited[start] = 1

    while queue:
        # queue의 맨 앞 요소를 꺼냄
        now = queue.pop(0)
        print(now, end=' ')

        # 인접한 노드들을 queue에 추가
        for next in range(5):
            # 연결 안되어 있으면
            if graph[now][next] == 0:
                continue

            # 방문했던 곳이면면
            if visited[next]:
                continue

            queue.append(next)
            # bfs 이므로 여기서 방문 체크를 해주어도 상관없다.
            visited[next] = 1


print('bfs = ', end='')
bfs(0)
