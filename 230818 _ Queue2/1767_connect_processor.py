'''
배열의 1은 맥시노스 존재
가장자리로 전선을 빼야 함
전선 교차 불가, 직선으로만 연결 가능
가장자리는 이미 전원이 연결된 것
최대한 많은 core 전원 연결하고 그 경우의 전선 길이 최소 합
연결된것 : 2 , 전선 : 3
1. 최대한 많은 core 연결하기 -> 무엇으로 구현할까
==>

'''
def cc():
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    stack = [] # 돌아갈 길
    which = []
    for i in range(1,N-1): # 가장자리 제거
        for j in range(1,N-1): # 가장자리 제거
            if maxinos[i][j] == 1:
                which.append((i,j))

    while True:
        # 한 방향 선택해서 가기 + 막히면 방향 바꾸기

    print(which)




T = int(input())

for tc in range(1, T + 1):
    N = int(input()) # 다음 N줄 (NxN 배열)
    maxinos = [list(map(int, input().split())) for _ in range(N)]

    cc()

    ans = 0

    print(f'#{tc} {ans}')