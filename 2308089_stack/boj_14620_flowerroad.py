N = int(input()) # 화단의 한 변의 길이
land = [list(map(int, input().split())) for _ in range(N)]
# 0이면 뭔가 있을 수 있는데 1이면 없음
can_land = [[0] * (N-2) for _ in range(N-2)]
cost_arr = [[0] * (N-2) for _ in range(N-2)]

# 오 아 왼 위
di = [0,1,0,-1]
dj = [1,0,-1,0]

cost = []

# cost_arr
for i in range(1, N - 1):
    for j in range(1, N - 1):
        cost = 0 # 5개 가격
        cost += land[i][j]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            cost += land[ni][nj]
        cost_arr[i - 1][j - 1] = cost

ans = 0

for _ in range(3):
    min_v = 1e9
    for i in range(N-2):
        for j in range(N-2):
            if can_land[i][j] == 0:
                if min_v >= cost_arr[i][j]:
                    min_v = cost_arr[i][j]
                    for k in range(4):
                        ni = i + di[k]
                        nj = j + dj[k]
                        if 0 < ni < (N - 2) and 0 < nj < (N - 2):
                        # if 0 < ni < (N - 2) and 0 < nj < (N - 2) and cost_arr[i][j] <= cost_arr[ni][nj]:
                            cost_arr[ni][nj] = 0
                            can_land[ni][nj] = 1
    ans += min_v

print(ans)

        # # 심을 수 있는지?
        # if can_land[i][j] == 0:
        #     for k in range(4):
        #         ni = i + di[k]
        #         nj = j + dj[k]
        #         if can_land[ni][nj] == 0:
        #             cnt += 1
        #
        #     # 아래는 심기
        #     if cnt == 4: # 심기 가능
        #         cost += land[i][j]
        #         can_land[i][j] = 1
        #         print(i, j)
        #         for k in range(4):
        #             ni = i + di[k]
        #             nj = j + dj[k]
        #             can_land[ni][nj] = 1
        #             cost += land[ni][nj]
        #         print(cost)
        #         if cost < min_cost:
        #             min_cost = cost

