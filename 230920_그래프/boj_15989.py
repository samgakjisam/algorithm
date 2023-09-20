'''
순서만 다른 것은 같은 것으로 친다. -> 조합
1. 1,2,3 의 합 -> 중복조합
2. 완전탐색 -> 일단 함 고 -> n이 10000보다 작거나 같기 때문에 완탐은 불가
=> 중복조합
3. DP
'''
# 시간초과
# def f(o,tw,th,N,s):
#     if s == N:
#         if [o,tw,th] not in num_arr:
#             num_arr.append([o,tw,th])
#         return
#     if s > N: # 초과될 때도 계속 가는 거 때문에 뎁스 초과
#         return
#     else:
#         f(o+1, tw, th, N, s+1)
#         f(o, tw+1, th, N, s+2)
#         f(o, tw, th+1, N, s+3)
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     num_arr = []
#     f(0, 0, 0, N, 0)
#     print(len(num_arr)

# DP
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    dp = [0] * 10001
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    dp[4] = 4
    dp[5] = 5
    if N > 4:
        for i in range(5,N+1):
            dp[i] = dp[i-3] + dp[3]

    print(dp[N])