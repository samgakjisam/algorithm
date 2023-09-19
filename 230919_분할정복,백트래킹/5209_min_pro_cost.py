# 순열
def perm(i,N,p):
    global min_v
    if p >= min_v:
        return

    if i == N: # 다 구함
        if min_v > p:
            min_v = p
        return
    else:
        for j in range(N):
            if used[j] == 0: # 안썼으면
                used[j] = 1
                perm(i+1, N, p+arr[i][j])
                used[j] = 0 # 풀어줘


T = int(input())

for tc in range(1, T + 1):
    N = int(input()) # 제품 수
    # 행은 상품, 열은 공장, 요소는 생산비용을 나타냄
    arr = [list(map(int, input().split())) for _ in range(N)]
    used = [0] * N
    min_v = 1e9
    # 공장(열)에 따라 순열 구하기
    perm(0,N,0)
    print(f'#{tc} {min_v}')