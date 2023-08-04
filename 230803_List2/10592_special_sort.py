T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    result_arr = [] # 정렬한 거 저장

    def SelectionSort(a, n):
        for i in range(n-1):
            min_idx = i
            for j in range(i + 1, n):
                if a[min_idx] > a[j]:
                    min_idx = j
            a[i], a[min_idx] = a[min_idx], a[i]
        return a

    arr_s = SelectionSort(arr, N)

    for i in range(0, 10):
        if i % 2 == 0: # 큰 수
            result_arr.append(arr_s.pop(-1))
        else: # 작은 수
            result_arr.append(arr_s.pop(0))

    print(f'#{tc} ',end = '')
    print(*result_arr)