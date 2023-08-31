'''
비트 연산 or 조합
'''
def f(n,r,s): # 조합 만들기
    global cnt
    if s > K: # K보다 합이 크면
        return
    if r == 0: # 다 만들었을 때
        if s == K:
            cnt += 1
    else:
        f(n-1,r-1,s+A[n-1])
        f(n-1,r,s)

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = 0

    for i in range(1,N+1):
        c = [0] * i
        f(N,i,0) # nCr, s는 합
