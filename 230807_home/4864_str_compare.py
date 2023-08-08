# itoa() 구현

T = int(input())
for tc in range(1, T + 1):
    s1 = list(map(str, input())) # 길이 N
    s2 = list(map(str, input())) # 길이 M
    N = len(s1)
    M = len(s2)
    result = 0

    for i in range(M - N + 1):
        cnt = 0
        for j in range(N):
            if s1[j] == s2[i + j]:
                cnt += 1
            else:
                cnt = 0
                continue
        if cnt == N:
            result = 1
            break
    print(f'#{tc} {result}')
