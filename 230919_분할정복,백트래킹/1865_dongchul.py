'''
순열로 일을 정해준다.
최대 확률을 고른다.
'''
def perm(i,N,g):
    global max_v
    if g <= max_v:
        return
    if i == N: # 다 고름
        if max_v < g:
            max_v = g
        return
    else:
        for j in range(N):
            if u[j] == 0:
                u[j] = 1
                perm(i+1,N,g*arr[i][j] / 100)
                u[j] = 0
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # i번 째 사람이 j번 째 일을 성공할 확률
    u = [0] * N
    p = [0] * N
    max_v = 0

    perm(0,N,1)
    ans = max_v * 100
    print(f'#{tc} {ans:.6f}')