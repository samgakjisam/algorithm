'''
소수점 아래 12자리 이내
13자리 이상은 overflow
'''

T = int(input())

for tc in range(1, T +1):
    N = float(input())
    ans = ''

    zari = 1.0  # 초기 자리수

    while N != 0.0:
        hh = 2 ** (-zari)
        if hh <= N:
            ans += '1'
            N -= hh
        else:
            ans += '0'
        zari += 1
        if zari > 12:  # 13자리 이상일 때
            ans = 'overflow'
            break

    print(f'#{tc} {ans}')