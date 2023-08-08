arr = [55, 7, 78, 12, 42]

def bubble_sort(arr, N): # 정렬할 List, 배열 원소 수
    for i in range(N - 1, 0, -1): # 뒤에 가장 큰 수 넣기 위해서 N이 아니고 N-1이여야지...
        # print(i) # N이 아니고 N-1이여야지... i = 1까지만 해도 되는게 어차피 0번째 인덱스는 정렬되있을 거임
        for j in range(i): # i 전까지 양쪽을 비교하겠다.
            if arr[j] > arr[j + 1]: # j번 째 원소가 j + 1 번 째 원소보다 크면
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # 서로 교환
    return arr

print(bubble_sort(arr, len(arr)))