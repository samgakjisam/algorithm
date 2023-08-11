def rot_90(arr, N):
    new_arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_arr[j][N - 1 - i] = arr[i][j]
    return new_arr

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    arr_90 = rot_90(arr, N)
    arr_180 = rot_90(arr_90, N)
    arr_270 = rot_90(arr_180, N)

    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(f'{arr_90[i][j]}', end='')
        print('', end= ' ')
        for j in range(N):
            print(f'{arr_180[i][j]}', end='')
        print('', end=' ')
        for j in range(N):
            print(f'{arr_270[i][j]}', end='')
        print('')