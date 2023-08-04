T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_90 = [[0]*N for _ in range(N)]
    arr_180 = [[0]*N for _ in range(N)]
    arr_270 = [[0]*N for _ in range(N)]

    # 90도 회전
    # i <- j
    # j <- 3 - i
    def rotation(a, N):
        a_90 = [[0]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                a_90[j][N - 1 - i] = a[i][j]
        return a_90

    arr_90 = rotation(arr, N)
    arr_180 = rotation(arr_90, N)
    arr_270 = rotation(arr_180, N)

    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(f'{arr_90[i][j]}', end='')
        print(' ', end='')
        for j in range(N):
            print(f'{arr_180[i][j]}', end='')
        print(' ', end='')
        for j in range(N):
            print(f'{arr_270[i][j]}', end='')
        print(' ', end='')
        print('')