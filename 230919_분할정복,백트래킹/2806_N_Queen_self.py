'''
경우의 수 구하기
서로 영향을 주면 안된다.
1. 위의 행에서 놓을 수 있는 위치에 놓기
2. 그 아래 행에서 놓을 수 있는 위치에 놓기
3. 안되면은 바로 리턴 때리기

다 놓고 결정 -> 놓으면서 결정 (안되면 바로 다음으로)
행을 따라 내려가면서 놓을 수 있는 열을 찾기
'''
def check(i,j):
    for k in range(3):
        ni = i + di[k]
        nj = j + dj[k]
        while 0<=ni<N and 0<=nj<N: # 벗어나지 않으면 실행
            if b[ni][nj] == 1: # 퀸 있으면
                return 0
            ni += di[k]
            nj += dj[k]
    return 1

def f(i,N):
    global cnt
    # 조건을 설정
    if i == N:# 끝 행까지 왔을 때 -> 가능
        cnt += 1
        return
    else:
        for j in range(N): # 열 순회
            if check(i,j):
                b[i][j] = 1
                f(i+1, N)
                # 갔다오면 풀어주기
                b[i][j] = 0

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    b = [[0] * N for _ in range(N)] # 체스 판
    cnt = 0
    # 왼위, 위, 오위
    di = [-1,-1,-1]
    dj = [-1,0,1]

    f(0,N) # 0번 행, 0번 열부터

    print(f'#{tc} {cnt}')
