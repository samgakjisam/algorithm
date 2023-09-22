from collections import deque

topni = [0]+[str(input()) for _ in range(4)]
K = int(input())
info = []
for i in range(K):
    n, dir = map(int, input().split())
    info[i].append([n,dir])

# 돌릴 거 선택
def sel(s, d):
    # 다음, 이전 거랑 맞물린 거 확인
    # 재귀로 구현
    if u[s] == 0:
        if s == 1:
            u
        if s == 4:

        else:



'''
1 ~ 2   t1[2], t2[6]
'''
for i in info:
    # 시작 톱니바퀴, 방향
    u = [0] * 4 # 돌았으면 1로
    sel(i[0], info[1])