# 날리는 최대 꽃가루 수 구하기
# 델타로 해보자

T = int(input())

for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    max_flower = 0
    flower = 0

    for i in range(N):
        for j in range(M):
            if max_flower <= flower:
                max_flower = flower
            flower = 0
            flower += arr[i][j]
            for k in range(4):
                if 0 <= (i + di[k]) < N and 0 <= (j + dj[k]) < M:
                    flower += arr[i+di[k]][j + dj[k]]
    print(f'#{tc} {max_flower}')