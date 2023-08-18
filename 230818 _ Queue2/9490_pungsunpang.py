T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    flower = [list(map(int, input().split())) for _ in range(N)] # N줄에 걸쳐
    # 오아왼위
    di = [0,1,0,-1]
    dj = [1,0,-1,0]

    max_v = 0

    for i in range(N):
        # 이동할 때 마다 summation 초기화
        for j in range(M):
            s = flower[i][j]
            for k in range(4):
                for p in range(1, flower[i][j] + 1): # 터뜨린 곳의 개수 만큼 퍼짐
                    ni = i + (di[k] * p)
                    nj = j + (dj[k] * p)
                    if 0<=ni<N and 0<=nj<M: # 퍼지는 게 범위 안벗어나면
                        s += flower[ni][nj]
            # 최대값 갱신
            if max_v <= s:
                max_v = s

    print(f'#{tc} {max_v}')