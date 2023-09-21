'''
최소한의 연료(가중치)
출발, 도착이 정해져 있음 -> 다익스트라
델타로 상하좌우 이동을 하면서 우선순위 큐에 저장하고 누적합을 통해 소비한 연료의 양을 계산한다.
1. 우선순위 큐에 출발지 enque
2. deque하고 for문으로 상하좌우 이동
3. 이동하려는 칸의 누적합이 이미 최소라면 continue
4. 더했는데
'''
# 등호 끼니까

# 힙 사용을 위한 import
import heapq

def dijkstra(si,sj):
    pq = [] # 우선순위 큐
    heapq.heappush(pq, (0,si,sj)) # 연료 기준으로 정렬
    # 방문기록(누적합 기록)
    fuel[si][sj] = 0

    while pq:
        f,i,j = heapq.heappop(pq)

        for k in range(4):
            ni = i+di[k]
            nj = j+dj[k]
            if 0<=ni<N and 0<=nj<N: # 배열을 벗어나지 않고
                if fuel[ni][nj] <= f:  # 기존에 있는 곳의 누적합이 더 작으면 => 갈 필요가 없음
                    continue

                # 기존 + 가려는 곳 연료소모량
                # 근데 높아지면 그만큼 더 더해야함
                new_fuel = f + 1
                if h[ni][nj] > h[i][j]: # 더 높아지면
                    new_fuel += (h[ni][nj] - h[i][j])

                # 다음 칸에 값이 지금의 new_fuel보다 작으면 -> 갈 필요없음
                if fuel[ni][nj] <= new_fuel:
                    continue

                # 누적합 저장
                fuel[ni][nj] = new_fuel

                heapq.heappush(pq, (new_fuel,ni,nj))


T = int(input())
for tc in range(1, T + 1):
    N = int(input()) # NxN 배열
    h = [list(map(int, input().split())) for _ in range(N)] # 높이 정보

    # 델타
    di = [0,1,0,-1]
    dj = [1,0,-1,0]

    # 누적합을 저장할 배열
    INF = 1e9
    fuel = [[INF] * N for _ in range(N)]

    # 출발 0,0 도착 N-1, N-1
    dijkstra(0,0)
    print(f'#{tc} {fuel[N-1][N-1]}')