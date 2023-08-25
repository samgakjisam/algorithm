T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # NxN 배열, 돌 두는 거 M
    arr = [list(map(int, input().split())) for _ in range(M)] # 돌 두는 거 리스트
    # [j][i][1 = B, 2 = W]

    pan = [[0] * (N+1) for _ in range(N+1)] # 행,열 0 패딩

    # i = 0, j = 0은 없는 걸로 쳐야 함

    # 초기 설정
    pan[N // 2][N // 2] = 2
    pan[N // 2][N // 2 + 1] = 1
    pan[N // 2 + 1][N // 2] = 1
    pan[N // 2 + 1][N // 2 + 1] = 2

    # 오 아 왼 위 오아 왼아 왼위 오위
    di = [0,1,0,-1,1,1,-1,-1]
    dj = [1,0,-1,0,1,-1,-1,1]

    for i in range(M):

        pan[arr[i][1]][arr[i][0]] = arr[i][2] # 이 좌표에 돌을 넣을 거임
        # 다른 색 돌이 어느 방향인지 확인
        # 그 방향으로 같은 색 돌 나올 때 까지 확인
        # 범위는 벗어나면 안되니까 0 < ni,nj < N + 1
        for k in range(8): # 방향 파악
            p = 1
            ni = arr[i][1] + di[k] * p
            nj = arr[i][0] + dj[k] * p
            # 그 쪽에 같은 색 돌이 있는지도 파악해야 함
            if 0 < ni < N + 1 and 0 < nj < N + 1 and arr[i][2] != pan[ni][nj] and pan[ni][nj] != 0:
                while pan[ni][nj] != arr[i][2]: # 같은 색 돌 나오면 멈추기
                    if pan[ni][nj] == 1: # 흑돌이면
                        pan[ni][nj] = 2 # 백돌로
                    elif pan[ni][nj] == 2: # 백돌이면
                        pan[ni][nj] = 1 # 흑돌로
                    p += 1
                print(pan)

