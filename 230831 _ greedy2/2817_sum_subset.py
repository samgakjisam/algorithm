'''
재귀로 부분 집합을 구하면서 합이 K가 되는 경우의 수 카운트
'''

def f(i,N,s,c):
    global cnt
    if s == K and c != 0:
        cnt += 1
        return
    elif s > K: # 이미 합 넘었으면
        return
    elif i == N: # 다 뽑았으면
        return
    else: # 뽑으면서 합하기
        f(i+1,N,s+arr[i],c+1) # 뽑은 거
        f(i+1,N,s,c) # 안 뽑은 거


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    leng = len(arr)
    cnt = 0

    # 부분집합 구하기
    f(0,leng,0,0)
    print(f'#{tc} {cnt}')
