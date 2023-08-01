T = int(input())

for tc in range(1, T + 1):
    K, N, M = list(map(int, input().split()))
    bus_stop = [0] * (N + 1)
    charger_stop = list(map(int, input().split()))

    for i in charger_stop:
        bus_stop[i] = 1
    x = 0 # 위치
    cnt = 0 # 충전 횟수
    no = 0
    while True:
        if no == K: # for문 안의 no가 K와 같아지면 더 이상 갈 수 없음
            cnt = 0
            break
        no = 0 ###### For 문 돌릴 때 초기화를 잘 해야 한다.
        x += K  # 최대 거리 이동
        if N <= x:
            break
        # 최대까지 갔을 때 그 자리 충전기
        if bus_stop[x] == 1:
            cnt += 1
        # 최대까지 갔는데 충전기 X
        elif bus_stop[x] == 0:
            # 뒤로 이동
            for i in range(K):
                x -= 1 # 뒤로 이동
                no += 1 # 이게 K가 되면 더 이상 갈 수 없음
                # 충전소 발견
                if bus_stop[x] == 1:
                    cnt += 1
                    break

    print(f'#{tc} {cnt}')