T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input()))
    cnt = 0
    max_cnt = 0
    for i in range(N):
        if lst[i] == 0:
            if max_cnt < cnt:
                max_cnt = cnt
            cnt = 0
        else:
            cnt += 1
        if max_cnt < cnt:
            max_cnt = cnt

    print(f'#{tc} {max_cnt}')

# # 오답
#     T = int(input())
#
#     for tc in range(1, T + 1):
#         N = int(input())
#         lst = list(map(int, input()))
#         cnt = 0
#         max_cnt = 0
#         for i in range(N):
#             if lst[i] == 1:
#                 cnt += 1
#                 if i == (N - 1):
#                     max_cnt = cnt ===> cnt가 더 작을수도 있잖아
#             else:
#                 if i != 0 and lst[i - 1] == 1:
#                     max_cnt = cnt
#                 cnt = 0
#         print(f'#{tc} {max_cnt}')