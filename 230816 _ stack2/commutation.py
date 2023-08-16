def f(i, N):
    global cnt
    cnt += 1
    if i == N:
        print(A)
    else:
        # 자리 바꾸기(자신부터 오른쪽 끝까지, 왼쪽으로 바꾸면 중복이됨)
        for j in range(i, N):
            A[i], A[j] = A[j], A[i]
            f(i+1, N)
            s +=
            A[i], A[j] = A[j], A[i] # 원상복구


A = [1,2,3]
cnt = 0
f(0,3)
print(cnt)