# 인접행렬
# 장점 : 구현이 쉽다.
# 단점 : 메모리 낭비
#       0도 표시를 하기 때문에
graph = [
    [0,1,0,1,0],
    [1,0,1,1,1],
    [0,1,0,0,0],
    [1,1,0,0,1],
    [0,1,0,1,0]
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
        # 큰 수부터 방문
        # for next in range(5):

        # 작은 수부터 방문
        for next in range(4,-1,-1):
            # 연결이 안되어 있다면 continue
            # 코드 스타일 차이 -> 할 수 없는 조건(pass 조건)을 넣는다.
            if graph[now][next] == 0:
                continue

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
    for next in range(5):
        if graph[now][next] == 0:
            continue

        if visited[next]:
            continue

        dfs(next)

print('dfs 재귀 = ', end='')
dfs(0)