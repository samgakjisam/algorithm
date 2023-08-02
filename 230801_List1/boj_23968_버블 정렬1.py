N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

cnt = 0

for i in range(N - 1, -1, -1): # 마지막 인덱스부터(N-1부터 0까지)
    for j in range(i): # 마지막 인덱스 전까지
        if A[j] > A[j + 1]:
            A[j], A[j + 1] = A[j + 1], A[j]
            cnt += 1
        if cnt == K:
            print(A[j], A[j + 1])
            break
    if cnt == K:
        break

if cnt < K:
    print(-1)        

