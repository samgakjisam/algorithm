'''
3
1 2 3
4 5 6
7 8 9
'''

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

max_v = 0 # 모든 원소가 0 이상이라면
for i in range(N): # 모든 원소 arr[i][j]에 대해...
    for j in range(N):
        # arr[i][j] 중심으로
        s = arr[i][j]
        for p in range(1, m): # 상하좌우 방면으로 m씩 이동했을 때
            for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                ni, nj = i+di*p, j+dj*p
                if 0 <= ni < N 0 <= nj < N:     # 배열을 벗어나지 않으면
                    s += arr[ni][nj]
        # 여기까지 주변 원소를 포함한 합
        if max_v < s: # s > max_v 하지말고 아래랑 맞춰서 해
            max_v = s