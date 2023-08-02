T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    colored_area = [[0] * 10] * 10 ### 이렇게 하면 하나의 배열만 같이 참조한다.
    colored_area = [[0]*10 for _ in range(10)] ### 이렇게 해야 10 x 10 만들어짐
    cnt = 0

    for area in range(N):
        r_lh, c_lh, r_rl, c_rl, color = map(int, input().split())
        for i in range(r_lh, (r_rl + 1)):
            for j in range(c_lh, (c_rl + 1)):
                colored_area[i][j] += color
                if colored_area[i][j] == 3:
                    cnt += 1

    print(f'#{tc} {cnt}')