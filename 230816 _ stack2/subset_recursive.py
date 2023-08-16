def f(i, N):
    global cnt
    cnt += 1
    if i == N:
        # print(bit)
        print(bit, end=' ')
        for j in range(N):
            if bit[j]:
                print(A[j], end=' ')
        print()
        return

    else:
        bit[i] = 1
        f(i + 1, N)
        bit[i] = 0
        f(i + 1, N)
        return
cnt = 0
A = [1,2,3]
bit = [0] * 3
f(0, 3)
print(cnt)