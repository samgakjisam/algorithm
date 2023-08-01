T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N-1, 0 , -1): # i 구간의 마지막 원소
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(arr)
    print(f'#{tc}', *arr) # *arr는 배열 언패킹 !!!
