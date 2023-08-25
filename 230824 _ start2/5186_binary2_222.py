T = int(input())

for tc in range(1, T + 1):

    N = float(input())
    ans = ''
    i = 0

    while i < 12 and N != 0:
        N *= 2
        if N >= 1.0:
            ans += '1'
            N -= 1.0
        else:
            ans += '0'
        i += 1
    if N == 0:
        print(f"#{tc} {ans}")
    else:
        print(f"#{tc} overflow")