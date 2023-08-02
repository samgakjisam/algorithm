T = int(input())

for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_kill = 0
    kill = 0

    for i in range(N):
        for j in range(N):
            kill = 0
            for k in range(M):  # 아래
                for p in range(M):  # 옆
                    if (0 <= (i + k) < N) and (0 <= (j + p) < N):
                        kill += arr[i + k][j + p]
                    else:
                        continue
            if max_kill <= kill:
                max_kill = kill

    print(f'#{tc} {max_kill}')


    # for j in range(N):
    #     if i <= N - 1: # 더 내려갈 수 있으면
    #         if j <= N - 1: # 옆으로 갈 수 있으면
    #             for k in range(M):  # 아래
    #                 for p in range(M):  # 옆
    #                     kill += arr[i + k][j + p]
    #         else: # 옆으로 못가면
    #             for k in range(M):  # 아래
    #                 kill += arr[i + k][j]
    #     else: # 못내려가면
    #         if j <= N - 1: # 옆으로 갈 수 있으면
    #             for p in range(M):  # 옆
    #                 kill += arr[i + k][j]
    #         else: # 옆으로 못가면
    #             kill += arr[i][j]