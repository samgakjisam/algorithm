# 인접리스트
# 갈 수 있는 지점만 저장하자
# 주의사항
#       - 각 노드마다 갈 수 있는 지점의 개수가 다름
#         -> range 쓸 때 index 조심
# 메모리가 인접행렬에 비해 훨씬 효율적이다.
# 딕셔너리로도 인접리스트를 쓸 수 있다.(파이썬)
graph_dict = {
    '0' : [1,3],
    '1' : [0,2,3,4],
    '2' : [1],
    '3' : [0,1,4],
    '4' : [1,3]
}

graph = [
    [1,3],
    [0,2,3,4],
    [1],
    [0,1,4],
    [1,3]
]

# if arr[0][1] == 1:
    # 갈 수 있다.
# DFS
# stack
def dfs_stack(start):
    visited = []
    stack = []
    stack.append(start)
    while stack: # 스택이 빌 때까지
        now = stack.pop()
        # 이미 방문한 지점이라면 continue
        if now in visited:
            continue

        # 방문하지 않은 지점이라면, 방문 표시
        visited.append(now)

        # 갈 수 있는 곳들을 stack에 추가
        # len(graph[now])
        for to in range(len(graph[now]) - 1,-1,-1):
            # 연결이 안되어 있다면 continue @@ 이 조건이 이제 필요없음
            # 코드 스타일 차이 -> 할 수 없는 조건(pass 조건)을 넣는다.
            # if graph[now][next] == 0:
            #     continue

            next = graph[now][to] ##

            # 방문한 지점이라면 stack에 추가하지 않음
            if next in visited:
                continue

            stack.append(next)

    return visited

print('dfs stack = ', end='')
print(*dfs_stack(0))


# 재귀
# MAP 크기(길이)를 알 때 append 형식 말고 아래와 같이 사용하면 훨씬 빠르다.
visited = [0] * 5
path = [] # 방문 순서 기록

def dfs(now):
    visited[now] = 1 # 현재 지점 방문 표시
    print(now, end= ' ')

    # 인접한 노드들을 방문
    for to in range(len(graph[now])):
        # if graph[now][next] == 0:
        #     continue

        next = graph[now][to] ##

        if visited[next]:
            continue

        dfs(next)

print('dfs 재귀 = ', end='')
dfs(0)