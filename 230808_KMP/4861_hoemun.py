T = int(input())

# def find_h(s, leng, M):
#     idx = 0
#     ans = []
#     for i in range(0, leng - M + 1): # step을 목표 회문 길이로
#         cnt = 0
#         for j in range(M // 2):
#             if s[i + j] == s[i + M - j - 1]:
#                 cnt += 1
#             if cnt == M // 2:
#                 idx = i
#                 for p in range(idx, idx + M):
#                     ans.append(s[p])
#     return ''.join(ans)


for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N x N , 길이가 M인 회문
    arr = [list(map(str, input())) for _ in range(N)]  # 배열
    # print(f'#{tc}', end=' ')
    for i in range(N):
        for j in range(N):
            arr[i][j]

    for k in range(N):
        print(find_h(*arr[k], N, M), end='')