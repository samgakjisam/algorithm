T = 10

for x in range(1 ,T + 1):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    di = [-1, 0, 0] # 위 오 왼
    dj = [0, 1, -1] # 위 오 왼
    # 도착지점 -> end
    i = 99
    j = 0
    for p in range(100):
        if arr[99][p] == 2:
            j = p
    d = 0

    while True:
        if i == 0:
            break
        if j == 0 or j == 99 or (0 <= i + di[d] < 100 and 0 <= j + dj[d] < 100):
            # 왼쪽 끝이나 오른쪽 끝에 있을 때 if문 안으로 못들어옴
            # 좌우 loop
            if d == 0: # 위로 진행중일 때
                for k in range(1, 3):  # 방향 찾기
                    if 0 <= j+dj[k] < 100 and arr[i + di[k]][j + dj[k]] == 1:
                        d = k # 왼쪽이나 오른쪽 가능
                i, j = i + di[d], j + dj[d]

            elif d == 2: # 왼쪽으로 진행중일 때
                if arr[i + di[0]][j + dj[0]] == 1: # 위로 갈 수 있으면
                    d = 0
                i, j = i + di[d], j + dj[d]

            elif d == 1: # 오른쪽으로 진행중일 때
                if arr[i + di[0]][j + dj[0]] == 1:  # 위로 갈 수 있으면
                    d = 0
                i, j = i + di[d], j + dj[d]

    print(f'#{tc} {j}')