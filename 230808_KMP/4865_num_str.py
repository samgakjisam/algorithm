T = int(input())

for tc in range(1, T + 1):
    str1 = str(set(list(str(input()))))
    N = len(str1)
    str2 = str(input())
    M = len(str2)
    str1 = set(list(str1))
    print(str1)
    max_v = 0

    for i in range(N):
        cnt = 0
        for j in range(M):
            if str2[j] == str1[i]:
                cnt += 1
                if cnt > max_v:
                    max_v = cnt

    print(f'#{tc} {max_v}')
