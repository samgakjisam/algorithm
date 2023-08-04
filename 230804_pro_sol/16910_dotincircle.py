T = int(input())

for tc in range(1, T + 1):
    r = int(input())

    ans = []
    cnt = 0
    for x in range(-r, r + 1):
        for y in range(-r ,r + 1):
            if x ** 2 + y ** 2 <= (r ** 2):
                cnt += 1

    print(f'#{tc} {cnt}')