def get_go(si,sj,dir):
    global can_op
    cnt = 0
    i = si
    j = sj
    ro = dir
    while cnt != 4:
        # 반시계 90도 회전
        if ro == 0:
            ro = 3
        else:
            ro -= 1
        # 앞이 범위를 벗어나지 않을 때
        if 0<=i+di[ro]<N and 0<=j+dj[ro]<M:
            # 그 앞이 0이면(청소가 되지 않은 부분이면)
            if bang[i+di[ro]][j+dj[ro]] == 0:
                # 전진할 좌표와 바라보는 방향 리턴
                return i+di[ro], j+dj[ro], ro
        cnt += 1

N, M = map(int, input().split())

i, j, dir = map(int, input().split()) # 좌표, 바라보는 방향

# dir 북,동,남,서 -> 반시계면 -1씩 해줘야겠다.
di = [-1,0,1,0]
dj = [0,1,0,-1]

# N는 행, M은 열
# 요소가 1이면 벽, 0이면 청소되지 않은 부분
# 청소를 하면 'C'로 바꾸자
bang = [list(map(int, input().split())) for _ in range(N)]

# 뒤쪽 칸이 벽이라 후진을 할 수 없으면 0으로 변경
can_op = 1
ans = 0

while can_op:
    # 현재 칸 청소
    if bang[i][j] == 0:
        ans += 1
        bang[i][j] = 'C'
    # 주변 네 칸 탐색
    cnt = 0  # 청소가 되지 않은 빈 칸
    for k in range(4):
        ni = i+di[k]
        nj = j+dj[k]
        if 0<=ni<N and 0<=nj<M:
            if bang[ni][nj] == 0: # 청소되지 않은 빈칸
                cnt += 1

    # 청소되지 않은 빈 칸이 있는 경우
    if cnt:
        # 반시계 방향 90도 회전 + 그 곳에 청소되지 않은 빈 칸이 있으면 전진
        i,j,dir = get_go(i,j,dir)
    # 청소되지 않은 빈 칸이 없는 경우
    else:
        # 반복문을 빠져나온다면 청소되지 않은 빈 칸이 없는 경우
        # 후진 할 수 있으면 -> 'C'이면 -> 후진 좌표, dir 리턴
        # 후진 할 수 없으면 -> 1이면 -> 원래 좌표, dir 리턴 + can_op = 0
        # 뒤 돌기
        ########## 임시 방향 ==> 바라보는 방향을 유지한 채 후진해야 한다.
        ro = 0
        if dir == 0:
            ro = 2
        elif dir == 1:
            ro = 3
        else:
            ro = dir - 2
        # 범위 벗어나면
        if 0 <= i + di[ro] < N and 0 <= j + dj[ro] < M:
            if bang[i + di[ro]][j + dj[ro]] == 1:
                can_op = 0
            else:
                i = i + di[ro]
                j = j + dj[ro]
        else:
            can_op = 0

print(ans)
