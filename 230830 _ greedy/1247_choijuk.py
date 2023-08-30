def cal(p):
    s = 0
    s = s + (abs(ci - p[0][0]) + abs(cj - p[0][1]))
    for k in range(1,N):
        s = s + (abs(p[k][0] - p[k-1][0]) + abs(p[k][1] - p[k-1][1]))
        if k == N-1:
            s = s + (abs(hi - p[k][0]) + abs(hj - p[k][1]))
    return s

def perm(i,N):
    global min_v
    if i == N:
        x = cal(p)
        if min_v > x:
            min_v = x
        return
    else:
        for j in range(N):
            if used[j] == 0:
                used[j] = 1
                p[i][0], p[i][1] = info[2*j], info[2*j+1]
                perm(i+1,N)
                used[j] = 0

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    info = list(map(int, input().split()))


    ci = info.pop(0)
    cj = info.pop(0)
    hi = info.pop(0)
    hj = info.pop(0)

    used = [0] * N
    p = [[0,0] for _ in range(N)]

    min_v = 1e9
    perm(0,N)

    print(f'#{tc} {min_v}')