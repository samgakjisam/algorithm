'''
1. 그래프 탐색(BFS) -> 최소니까
2. DP
중간 연산 결과는 항상 백만 이하
'''

# def f(N,M,s,c):
#     global min_v
#     if N == M:
#         if min_v > c:
#             min_v = c
#         return
#     if min_v < c: # 이미 횟수가 더 많으면
#         return
#     if N < 0: # 음수되면
#         return
#     if N >= M * 2:
#         return
#     else:
#         f(N,M,s+1,c+1)
#         f(N,M,s-1,c+1)
#         f(N,M,s*2,c+1)
#         f(N,M,s-10,c+1)
def bfs(start, end):
    q = []
    visited[start] += 1
    q.append(start)

    while q:
        start = q.pop(0)
        if start == end:
            break
        for i in [1, -1, start, -10]:
        # 안되는 조건부터
            if start + i < 0:
                continue
            if start + i >= 1000000:
                continue
            if start + i in q:
                continue
            if visited[start+i] != -1:
                continue
            visited[start+i] = visited[start] + 1
            q.append(start+i)

    return visited[end]



T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    visited = [-1] * 1000001

    print(f'#{tc} {bfs(N,M)}')