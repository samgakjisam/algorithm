T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    bus = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    C = [int(input()) for _ in range(P)] # 버정

    cnt_arr = [0] * 5001

    for nosun in range(N):
        for j in range(bus[nosun][0], bus[nosun][1] + 1): # A ~ B
            cnt_arr[j] += 1

    print(f'#{tc} ', end='')
    for i in C:
        print(f'{cnt_arr[i]} ', end='')
    print()