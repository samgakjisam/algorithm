from collections import deque

def bfs(s):

    q = deque()
    q.append(s)

    while q:
        i = q.popleft()
        for j in range(N):
            if arr[i][j]:
                q.append(j)

T = int(input())

for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(N)]
    # [출][도] = 사용량 0 -> ... -> N -> 0

    min_v = 1e9

    bfs(0)