'''
5개 이상
'''

T = int(input())

for tc in range(1, T + 1):
    N = int(input()) # NxN
    arr = [list(map(str, input())) for _ in range(N)]

    # 오 아 왼 위 오아 왼아 왼위 오위
    di = [0, 1, 0, -1, 1, 1, -1, -1]
    dj = [1, 0, -1, 0, 1, -1, -1, 1]

    ans = 'NO'
    flag = 0

    for i in range(N):
        if flag:
            break
        for j in range(N):
            if flag:
                break
            if arr[i][j] == 'o':
                for k in range(8):
                    if flag:
                        break
                    cnt = 0 # 방향 바꿀 때 초기화
                    for p in range(1, 5):
                        ni = i + di[k] * p
                        nj = j + dj[k] * p
                        if 0 <= ni < N and 0 <= nj < N:
                            if arr[ni][nj] == 'o':
                                cnt += 1
                    if cnt == 4:
                        ans = 'YES'
                        flag = 1
                        break

    print(f'#{tc} {ans}')