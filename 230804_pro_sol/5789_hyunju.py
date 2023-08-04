T = int(input())

for tc in range(1, T + 1):
    N, Q = map(int, input().split()) # 상자, 횟수
    arr = [0] * N

    for i in range(1, Q + 1): # 1부터 Q까지 ==> i
        L, R = map(int, input().split())
        for j in range(L, R + 1):
            arr[j - 1] = i

    print(f'#{tc}', *arr)