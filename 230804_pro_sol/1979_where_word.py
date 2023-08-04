T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    can_r = 0
    can_c = 0

    for i in range(N):
        cnt_r = 0
        cnt_c = 0
        for j in range(N):
            if puzzle[i][j]:
                cnt_r += 1 # 먼저 더하고
            if j == N-1 or puzzle[i][j]==0: # 벽보고
                if cnt_r == K: # 판별
                    can_r += 1
                cnt_r= 0
            if puzzle[j][i]:
                cnt_c += 1 # 먼저 더하고
            if j == N-1 or puzzle[j][i]==0: # 벽보고
                if cnt_c == K: # 판별
                    can_c += 1
                cnt_c= 0

    print(f'#{tc} {can_r + can_c}')