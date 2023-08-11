T = int(input())

#     for i in range(0, leng - M + 1): # step을 목표 회문 길이로
#         cnt = 0
#         for j in range(M // 2):
#             if s[i + j] == s[i + M - j - 1]:
#                 cnt += 1
#             if cnt == M // 2:
#                 idx = i

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N x N , 길이가 M인 회문
    arr = [list(map(str, input())) for _ in range(N)]  # 배열
    new_arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_arr[i][j] = arr[j][i]
    print(f'#{tc}', end=' ')

    for i in range(N):
        cnt = 0
        idx = 0
        for j in range(0, N - M + 1):
            for k in range(M // 2):
                if arr[i][j + k] == arr[i][j + M - k - 1]:
                    cnt += 1
                if cnt == M // 2:
                    idx = j
                    print(''.join(arr[i][idx:]))

    for i in range(N):
        cnt = 0
        idx = 0
        for j in range(0, N - M + 1):
            for k in range(M // 2):
                if new_arr[i][j + k] == new_arr[i][j + M - k - 1]:
                    cnt += 1
                if cnt == M // 2:
                    idx = j
                    print(''.join(new_arr[i][idx:]))

    # print(arr)
    #
    # '''
    # 처음과 마지막만 비교하면서 들어가면서 같으면 추출
    # '''
    #
    # for i in range(N):
    #     cnt = 0
    #     idx = 0
    #     for j in range(0, N - M + 1):
    #         print(arr[j][i])
    #         # for k in range(M // 2):
    #         #     if arr[j+k][i] == arr[j + M - k - 1][i]:
    #         #         cnt += 1
    #         #     if cnt == M // 2:
    #         #         idx = j
    #         #         print(arr[idx:][i])
