'''

'''

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]

    ans = 'no'
    flag = 0 # 1은 찾음, 2는 다른 거 찾기

    for i in range(N):
        if flag == 1:
            break
        for j in range(N):
            if arr[i][j] == '#':
                k = 1
                edge_r = 1
                edge_c = 1
                cnt = 0
                for k in range(1, N-j):
                    if arr[i][j + k] == '#':
                        edge_r += 1
                    else:
                        break
                for k in range(1, N-i):
                    if arr[i + k][j] == '#':
                        edge_c += 1
                    else:
                        break
                if edge_r > 1 and edge_c > 1 and edge_c == edge_r:
                    for p in range(edge_r):
                        if flag == 2:
                            break
                        for o in range(edge_c):
                            if arr[i + p][j + o] == '#':
                                cnt += 1
                            else:
                                flag = 2
                                break
                if cnt == edge_r * edge_c:
                    ans = 'yes'
                    flag = 1
                    break

    print(f'#{tc} {ans}')