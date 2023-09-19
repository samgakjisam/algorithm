'''
이진탐색

'''
def bs(i,l,m,r):
    # global le, ri
    if A[m] == i:
        return
    if i < A[m]: # 왼쪽에 있다는 거
        # le += 1
        bs(i, l, (l+m-1)//2, m-1)
    else: # 오른쪽에 있다는 거
        bs(i, m+1, (r+m+1)//2, r)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    for i in B:
        l = 0
        r = N-1 # 마지막 인덱스
        m = (l+r) // 2
        le = 0
        ri = 0
        bs(i,l,m,r)
