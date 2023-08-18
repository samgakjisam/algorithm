def bfs(st, link):
    # 큐, 방문기록
    q = []
    visited = [0] * 101 # 사람 수
    # 시작점
    q.append(st)
    visited[st] = 1
    ans = 0

    while q:
        s = q.pop(0) # 시작
        for w in range(101): # 배열 탐색
            if link[s][w] == 1 and visited[w] == 0: # 방문한적없고 연락가능
                q.append(w)
                visited[w] = visited[s] + 1 # 마지막은 최대값일 거임

    max_v = 0 # 최대값 구하기
    for i in range(101):
        if max_v <= visited[i]:
            max_v = visited[i] # 최대 값 갱신
            ans = i # 최대인 인덱스 갱신

    return ans



T = 10

for tc in range(1, T + 1):
    leng, st = map(int, input().split())
    link = [[0] * 101 for _ in range(101)] # 최대 인원 (번호 1 ~ 100)
    arr = list(map(int, input().split()))

    for i in range(leng): # link에 넣기
        if i % 2 == 0:
            link[arr[i]][arr[i+1]] = 1

    print(f'#{tc} {bfs(st, link)}') # 시작점, 연결된 정보보