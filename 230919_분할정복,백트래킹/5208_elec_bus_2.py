def f(i,c,N, cnt): # 현재위치, 배터리용량, 도착위치
    global min_v
    # 조건
    if i + c >= N: # 도착 할 수 있을 때
        if min_v > cnt:
            min_v = cnt
        return
    elif cnt >= min_v: # 도착 안했는데도 최소값보다 클 때
        return
    else:
        for j in range(1, c+1): # 갈 수 있는 곳
            f(i+j,bat[i+j],N,cnt+1)

T = int(input())

for tc in range(1, T + 1):
    bat = list(map(int, input().split())) # bat[0] = N
    min_v = 101

    f(1,bat[1],bat[0], 0)

    print(f'#{tc} {min_v}')