def bfs(si,sj,L):
    q = []
    visited = [[0] * M for _ in range(N)]
    q.append([si,sj])
    temp = []
    l = 0
    '''
    l을 큐에 쌓게 하지 않기 위해서 temp라는 배열을 따로 선언한다.
    갈 수 있는 방향을 모두 저장했을 때 l이 증가.
    q가 비어있을 거기 때문에 q에 temp를 모두 저장하고 temp를 초기화.
    l 증가
    큐가 비어있는데 l이 L과 같으면은 반복문을 종료한다.
    '''
    while q and l != L:
        i, j = q.pop(0) # 위치, 시간
        visited[i][j] = 1
        for k in tu[info[i][j]]:
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<N and 0<=nj<M and info[ni][nj] != 0 and visited[ni][nj] == 0: # 안 벗어나고 가는 곳 0 아니면
                # 돌아갈 수 있는 지 확인
                if (k+2) % 4 in tu[info[ni][nj]]: # 돌아갈 수 있으면
                    temp.append([ni,nj])
        if not q:
            q = temp
            temp = []
            l += 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 1:
                cnt += 1

    return cnt


T = int(input())

for tc in range(1, T + 1):
    N,M,R,C,L = map(int,input().split())

    info = [list(map(int, input().split())) for _ in range(N)]
    # 오아왼위
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    # 터널을 만났을 때 갈 수 있는 방향 (k)
    tu = [0,[0,1,2,3],[1,3],[0,2],[0,3],[0,1],[1,2],[2,3]]

    print(f'#{tc} {bfs(R,C,L)}')