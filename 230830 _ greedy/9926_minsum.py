'''
다 돌아보기
'''
# from collections import deque
#
# def bfs(si,sj):
#     q = deque()
#     dp = [0] * 3
#     q.append([si,sj])
#     ch = 0 #
#     while q:
#         i, j = q.popleft()
#         di = [0,1]
#         dj = [1,0]
#
#         for k in range(2): # 오른쪽 아래쪽으로 -> 이상한 데로 가면 최소 절대 안나옴
#             ni = i + di[k]
#             nj = j + dj[k]
#             if 0<=ni<N and 0<=nj<N:
#                 q.append([ni,nj])
#         q.append(ch)
#
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     bfs(0,0)

# def dfs(i,j):
#     stack = []
#     visited = [[0] * N for _ in range(N)]
#     visited[i][j] = 1
#     sum = 0
#     min_v = 1e9
#     while True:
#
#         di = [0,1]
#         dj = [1,0]
#
#         for k in range(2): # 오른쪽 아래쪽으로 -> 이상한 데로 가면 최소 절대 안나옴
#             ni = i + di[k]
#             nj = j + dj[k]
#             if ni == N-1 and nj == N-1:
#                 if min_v < sum:
#                     min_v = sum
#                 sum = 0
#             if 0<=ni<N and 0<=nj<N:
#                 stack.append([i,j])
#                 visited[i][j] = 1
#                 sum += arr[i][j]
#                 i,j = ni,nj
#                 break
#
#     return min_v
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     bfs(0,0)


def dfs(i,j):
    global min_v
    global s

    if i == N - 1 and j == N - 1:
        s += arr[i][j]
        if min_v > s:
            min_v = s
        return
    di = [0,1]
    dj = [1,0]

    s += arr[i][j]

    for k in range(2): # 오른쪽 아래쪽으로 -> 이상한 데로 가면 최소 안나옴
        ni = i + di[k]
        nj = j + dj[k]
        if 0<=ni<N and 0<=nj<N:
            temp = s
            dfs(ni,nj)
            s = temp


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_v = 1e9
    s = 0
    dfs(0,0)
    print(f'#{tc} {min_v}')