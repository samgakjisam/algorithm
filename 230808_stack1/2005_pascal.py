# N = 4
# tri = [0] * N
#
# # 배열 만들기
# for i in range(1, N + 1):
#     temp = [0] * i
#     for j in range(i):
#         temp[j] = 1
#     tri[i - 1] = temp
#
# # 파스칼
# for i in range(2, N):
#     for j in range(1, i):
#         tri[i][j] = tri[i - 1][j-1] + tri[i - 1][j]
#
# print(tri)

# print(pascal(1))

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    tri = [[1] * (i + 1) for i in range(N)]
    # tri = [0] * N
    # 배열 만들기
    # for i in range(1, N + 1):
    #     temp = [0] * i
    #     for j in range(i):
    #         temp[j] = 1
    #     tri[i - 1] = temp

    # 파스칼
    for i in range(2, N):
        for j in range(1, i):
            tri[i][j] = tri[i - 1][j-1] + tri[i - 1][j]
    print(f'#{tc}')
    for i in range(N):
        print(*tri[i])