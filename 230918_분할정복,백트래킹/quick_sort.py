def qsort(A, l, r):
    if l < r:
        s = partition(A, l, r)
        qsort(A, l, s-1)
        qsort(A, s+1, r)

def partition(A, l, r):
    p = A[l] # 가장 왼쪽 원소를 피봇으로 하는 경우
    i = l
    j = r
    while i <= j: # 교차되기 전까지



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input()))

    qsort(arr,0,len(arr)-1)

    ans = arr[N//2]

    print(f'#{tc} {ans}')