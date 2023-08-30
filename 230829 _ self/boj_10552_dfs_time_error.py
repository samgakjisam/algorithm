'''
위에서부터 아래 짬순
좋, 싫
P가 시작
갈 곳이 없으면 티비 변경 횟수 출력
계속 빙빙돌면 -1 출력
빙빙 돌 경우 info 내에 들리지 않는 곳이 있을 것
-> 빙빙 돌지 않아도 들리지 않는 곳이 있음
-> 스택에 그 도착지가 있으면 빠져나가면 될 듯
'''

# import sys
#
# def dfs(s):
#     global cnt
#     visited[s] = 1
#     stack = []
#     while True:
#         for w in range(1, M + 1):
#             if visited[w] == 0 and info[s][w] == 1:
#                 visited[w] = 1
#                 stack.append(s)
#                 s = w
#                 cnt += 1
#                 break
#         else:
#             # 빙빙 돌 경우는 스택에 쌓인 곳으로 도착할 수 있는 경우이다.
#             for j in stack:
#                 if info[s][j] == 1:
#                     cnt = -1
#                     break
#             break # 갈 곳 없을 때 돌아갈 필요가 없음
#     return cnt
#
# N,M,P = map(int, sys.stdin.readline().split())
#
# info = [[0] * (M + 1) for _ in range(M + 1)]
#
# for i in range(1, N + 1):
#     lik, hat = map(int, sys.stdin.readline().split())
#     info[hat][lik] = 1
#
# visited = [0] * (M + 1)
# cnt = 0
#
# dfs(P) # 시작
#
# print(cnt)

import sys

def dfs(s):
    visited[s] = 1
    cnt = 0
    while True:
        for j in info:
            if j[0] == s:
                if visited[j[1]] == 0:
                    visited[j[1]] = 1 # 도착지
                    s = j[1]
                    cnt += 1
                    break
                else:
                    cnt = -1
                    return cnt
        else: # 갈 데 없으면 나가
            break
    return cnt

N,M,P = map(int, sys.stdin.readline().split())

info = [0] * N

for i in range(N):
    lik, hat = map(int, sys.stdin.readline().split())
    info[i] = [hat,lik]

visited = [0] * (M + 1)

print(dfs(P)) # 시작


# import sys
# limit_number = 15000
# sys.setrecursionlimit(limit_number)
#
# def dfs(s):
#     global cnt
#     global flag
#
#     if flag == 1:
#         return
#
#     for i in range(1, M + 1):
#         if info[s][i] == 1:
#             if visited[i] == 0:
#                 cnt += 1
#                 dfs(i)
#             else:
#                 cnt = -1
#                 return
#     else: # 갈 곳이 없으면
#         flag = 1
#         return
#
# N,M,P = map(int, sys.stdin.readline().split())
#
# info = [[0] * (M + 1) for _ in range(M + 1)]
#
# for i in range(1, N + 1):
#     lik, hat = map(int, sys.stdin.readline().split())
#     info[hat][lik] = 1
#
# visited = [0] * (M + 1)
# cnt = 0
# flag = 0
#
# dfs(P) # 시작
#
# print(cnt)