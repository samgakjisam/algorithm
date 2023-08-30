N,M = map(int, input().split())

arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
stack = []

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

i = 0
j = 0
visited[0][0] = 1
stack.append([i,j])

while True :

    i,j = stack.pop()

    for k in range(4) :

        ni = i + di[k]
        nj = j + dj[k]

        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1 and visited[ni][nj] == 0:

            arr[ni][nj] = arr[i][j] + 1
            stack.append([ni,nj])
            visited[ni][nj] = 1

    if len(stack) == 0 :

        break

print(arr[N-1][M-1])