def jong_e(n):
    dp = [0] * (n + 1) # [0, 0, 0, 0]
    dp[1] = 1
    dp[2] = 3
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + (2 * dp[i - 2])

    return dp[n]


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    n = N // 10
    print(f'#{tc} {jong_e(n)}')