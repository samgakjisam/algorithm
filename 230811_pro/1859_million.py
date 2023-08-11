T = int(input())

for tc in range(1, T + 1):
    N = int(input()) # 날짜 개수
    price = list(map(int, input().split()))

    max_v = price[N - 1] # 마지막 요소
    get = 0 # 개수
    money = 0 # 갖고 있는 돈

    for i in range(N - 2, -1, -1): # 뒤에서부터 탐색
        if max_v < price[i]: # 같은 경우는 제외 (이득 없음)
            money += (get * max_v)
            get = 0
            max_v = price[i]  # 최대 값 바뀜

        else: # 조건이 잘 안되는 게 있음음
       # if price[i] <= price[i + 1]: # 뒤에거보다 작으면
            get += 1 # 개수 더하기
            money -= price[i] # 구매
            if i == 0: # 첫 요소로 갔을 때
                # get += 1 # 이미 위에서 더했음
                # money -= price[0] # 위에서 이미 함
                money += (get * max_v)

    print(f'#{tc} {money}')
