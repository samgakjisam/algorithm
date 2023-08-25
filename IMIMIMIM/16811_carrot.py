'''
크기 1 2 3
- 한 상자에 N / 2 까지 담을 수 있다.

- 당근 개수 차이 최소, 포장할 수 없으면 -1

- 3 파트로 자르기
'''




T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    carrot = list(map(int, input().split()))

    ans = 0

    # 당근 크기 배열
    size = [0] * 31
    size.append(0)

    # 사이즈 같은 거 몇 개 있는지
    for i in range(N):
        size[carrot[i]] += 1
        if size[carrot[i] + 1] > (N // 2):
            ans = -1 # 개수가 N/2보다 많으면 -1

    arr = []

    # 0 지우기
    for i in range(31):
        if size[i] == 0:
            continue
        arr.append(size[i])

    length = len(arr)

    min_v = 1e9

    for i in range(1,length - 1): # 앞 자르기 (얘부터 시작임, 하나 마진 둬야함)
        for j in range(i+1, length): # 뒤 자르기 (얘까지임)
            SML = [0, 0, 0]
            for k in range(0,i): # 0부터 i전 S
                SML[0] += arr[k]
            for k in range(i,j): # i부터 j까지
                SML[1] += arr[k]
            for k in range(j, length): # j부터 끝까지
                SML[2] += arr[k]
            if SML[0] <= N // 2 and SML[1] <= N // 2 and SML[2] <= N // 2:
                minus = max(SML) - min(SML)
                if min_v >= minus:
                    min_v = minus

    if min_v == 1e9:
        ans = -1
    else:
        ans = min_v

    print(f'#{tc} {ans}')






























    # for i in range(1, 31):
    #     # 사이즈 같은거 2개 이상
    #     if size[i] > 1:
    #         if where == 0: # S
    #             pass
    #         elif where == 1: # M
    #             if SML[0] < (N - size[i]) // 2:  # 근데 그 상자에 얼마 안담겨 있으면
    #                 ans = -1
    #                 break
    #         elif where == 2: # L
    #             if SML[0] + SML[1] < N - size[i]:
    #                 ans = -1
    #                 break
    #         elif where == 3:
    #             ans = -1
    #             break
    #         SML[where] += (size[i])
    #         where += 1 # 다음 상자로
    #
    #     # 하나만 있으머는
    #     elif size[i] == 1:
    #         if where == 2:
    #             SML[where] += 1
    #         else:
    #             if N % 3 == 1:
    #                 if SML[where] < N // 3:
    #                     SML[where] += 1
    #                 else:
    #                     where += 1
    #                     SML[where] += 1
    #             elif N % 3 == 2:
    #                 if SML[where] < (N // 3) + 1:
    #                     SML[where] += 1
    #                 else:
    #                     where += 1
    #                     SML[where] += 1
    #             elif N % 3 == 0:
    #                 if SML[where] < N // 3:
    #                     SML[where] += 1
    #                 else:
    #                     where += 1
    #                     SML[where] += 1
    #
    # if ans != -1:
    #     SML = SML[:3]
    #     ans = max(SML) - min(SML)
    #
    # print(f'#{tc} {ans}')