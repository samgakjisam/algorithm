def gin(p,N):
    s = 0
    for k in range(N-2):
        if p[k] == p[k+1] == p[k+2]:
            s = 1
        if (p[k] + 1 ==  p[k+1]) and (p[k+1] + 1 == p[k+2]):
            s = 1
    return s

def baby(i, N, X):
    global f
    if i == N:
        if gin(p,N):
            f = 1
    else:
        for j in range(N):
            if used[j] == 0:
                p[i] = X[j]
                used[j] = 1
                baby(i+1, N, X)
                used[j] = 0
    return f

T = int(input())

for tc in range(1, T + 1):
    card = list(map(int, input().split()))

    A = [] # 0,2,4,6,8,10 -> 먼저가져감
    B = [] # 1,3,5,7,9,11

    ans = 0
    f = 0

    for i in range(12):
        if i % 2 == 0:
            A.append(card[i])
            if i > 3:
                N = len(A)
                p = [0] * N
                used = [0] * N
                if baby(0,N,A):
                    ans = 1
                    break
        else:
            B.append(card[i])
            if i > 4:
                N = len(B)
                p = [0] * N
                used = [0] * N
                if baby(0,N,B):
                    ans = 2
                    break

    print(f'#{tc} {ans}')
