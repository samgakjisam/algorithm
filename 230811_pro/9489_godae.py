T = int(input()) # 사진 데이터 개수

for tc in range(1, T + 1):
    N, M = map(int, input().split()) # N x M 배열 # N행, M열
    pic = [list(map(int, input().split())) for _ in range(N)]
    jung_bok = [[0] * M for _ in range(N)]
    # 오 아
    di = [0,1]
    dj = [1,0]
    leng = 0
    max_leng = 0

    for i in range(N):
        for j in range(M):
                if pic[i][j] == 1:
                    for k in range(2):
                        p = 0
                        if max_leng <= leng:
                            max_leng = leng
                        leng = 0
                        while True:
                            ni = i + (di[k] * p)
                            nj = j + (dj[k] * p)
                            if 0 <= ni < N and 0 <= nj < M:
                                if pic[ni][nj] == 0:
                                    break
                                leng += 1
                                p += 1
                            else:
                                break

    print(f'#{tc} {max_leng}')
