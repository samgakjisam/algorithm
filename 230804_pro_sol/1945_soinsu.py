T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [2, 3, 5, 7, 11]
    cnt = [0] * 5

    while N != 1:
        for i in range(len(arr)):
            if N % arr[i] == 0:
                N = N / arr[i]
                cnt[i] += 1
    print(f'#{tc}', *cnt)
