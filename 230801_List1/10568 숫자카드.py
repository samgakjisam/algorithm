T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))
    cnt = [0] * 10

    for i in arr:
        cnt[i] += 1
    # max_card_cnt = 0
    max_num = 0
    for i in range(10):
        if cnt[max_num] <= cnt[i]: # 생각좀!~!
            max_num = i
        # if cnt[i] >= max_card_cnt:
        #     max_card_cnt = cnt[i]
        #     max_num = i

    print(f'#{tc} {max_num} {cnt[max_num]}')