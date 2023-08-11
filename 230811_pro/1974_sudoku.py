T = int(input())

for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    sol = 1

    for i in range(9):
        temp_r = [0] * 10
        temp_c = [0] * 10
        for j in range(9):

            if temp_r[arr[i][j]]: # 행
                sol = 0
            else:
                temp_r[arr[i][j]] = 1

            if temp_c[arr[j][i]]: # 열
                sol = 0
            else:
                temp_c[arr[j][i]] = 1

            if i % 3 == 0 and j % 3 == 0: # 3x3
                temp_s = [0] * 10
                for k in range(3):
                    for p in range(3):
                        if temp_s[arr[i + k][j + p]]:
                            sol = 0
                        else:
                            temp_s[arr[i + k][j + p]] = 1

    print(f'#{tc} {sol}')