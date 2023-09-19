def promising(i,j): # 위쪽 왼 대각, 위, 오 대각에 1이 있는지 확인해본다.
    for k in range(i):
        if arr[k][j]: # 같은 열에 이미 퀸이 있으면
            return 0
    # 대각선 확인 방법 1. 델타
    # 오 대
    ni, nj = i-1, j+1
    while 0 <= ni < N and 0 <= nj < N :
        if arr[ni][nj]:
            return 0
        ni -= 1
        nj += 1

    # 왼 대
    ni, nj = i-1, j-1
    while 0 <= ni < N and 0 <= nj < N:
        if arr[ni][nj]:
            return 0
        ni -= 1
        nj -= 1

    return 1

    # 확인 방법 2. -> 지원님 풀이 참고
    # 대각선 => abs(해당열 - 열) == 해당행 - 행 => 행은 무조건 해당행이 더 큼 (위로 탐색이니까까)

    # 확인 방법 3.

def f(i, N):
    global cnt
    if i == N: # N개의 퀸을 모두 놓으면
        cnt += 1
    else:
        # j열에 퀸을 놓기
        # i행 j열에 퀸을 놓을 수 있으면
        for j in range(N):
            if promising(i,j): # 놓을 수 있는 지 확인하러 가자
                arr[i][j] = 1 # 퀸을 놔
                f(i+1, N)
                arr[i][j] = 0 # 갔다오면 치워
    return

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)] # 체스판
    cnt = 0
    f(0,N)
    print(f'#{tc} {cnt}')