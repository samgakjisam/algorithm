for T in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max_v = 0
    dae_l_r = 0
    dae_r_l = 0
    row_sum = 0
    col_sum = 0
    for i in range(100):
        if max_v <= row_sum:
            max_v = row_sum
        if max_v <= dae_l_r:
            max_v = dae_l_r
        if max_v <= dae_r_l:
            max_v = dae_r_l
        row_sum = 0
        dae_l_r = 0
        dae_r_l = 0
        dae_l_r += arr[i][i]
        dae_r_l += arr[i][99 - i]
        for j in range(100):
            if max_v <= col_sum:
                max_v = col_sum
            col_sum = 0
            row_sum += arr[i][j]
            for k in range(100):
                col_sum += arr[k][j]
    print(f'#{tc} {max_v}')