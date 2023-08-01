arr = [55, 7, 78, 12, 42]

for i in range(len(arr), 0, -1): # 범위의 끝 위치를 지정(i)
    for j in range(i - 1): # i 전까지 i에 갖다놓는 거
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j] #####
        else:
            pass
        print(arr)
