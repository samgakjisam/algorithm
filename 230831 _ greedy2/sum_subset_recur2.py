'''
i번째 원소를 포함 or 미포함
찾고 중단해야 할 때는 ??
'''

def subset(i,N,s,c):
    if s == 0 and c != 0: # 합 0인데 공집합이 아니여야 함
        return 1
    elif i == N: # 마지막까지 갔는데도 목표가 안되면
        return 0
    else:
        if subset(i+1, N, s+arr[i], c+1):
            return 1
        if subset(i+1, N, s, c):
            return 1
        return 0

arr = [-1,3,-9,6,7,-6,1,5,4,-2]
# arr = [1,2,3,4,5]
N = len(arr)
bit = [0] * N
print(subset(0,N,0,0))
