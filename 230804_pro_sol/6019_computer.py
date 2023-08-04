T = int(input())

for tc in range(1, T + 1):
    D, A, B, F = map(int, input().split())

    ans = (D / (A + B)) * F

    print(f'#{tc} {ans}')