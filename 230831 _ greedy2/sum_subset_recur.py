'''
i번째 원소를 포함 or 미포함
'''

def subset(i,N):
    global cnt
    if i == N:
        s = 0
        for j in range(N):
            if bit[j]:
                s += arr[j]
        if s == 0:
            for j in range(N):
                if bit[j]:
                    print(arr[j], end = ' ')
            cnt += 1
            print()
    else:
        bit[i] = 1
        subset(i+1,N)
        bit[i] = 0
        subset(i+1, N)

arr = [-1,3,-9,6,7,-6,1,5,4,-2]
N = len(arr)
bit = [0] * N
cnt = 0
subset(0,N)
print(cnt)