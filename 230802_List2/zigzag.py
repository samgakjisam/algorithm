N = 2 # 행의 크기
M = 4 # 열의 크기

arr = [[0, 1, 2, 3], [4, 5, 6, 7]]
for i in range(N):
    for j in range(M):
        print(arr[i][j + ((M-1 - j*2) * (i % 2))]) # 이해가 안돼

        # if i % 2 == 1: # 홀수번 행인 경우
        #     print(arr[i][-j - 1])
        # else: # 짝수번 행인 경우 (0 포함)
        #     print(arr[i][j])