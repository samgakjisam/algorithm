'''
6               # 구역 수
5 2 3 4 1 2     # 각 구역의 인구
2 2 4           # 1번 구역에 인접한 구역 수, 인접 구역
4 1 3 6 5
2 4 2
2 1 3
1 2
1 2
'''

def f(g, N):    # 선거구를 탐새하는 bfs()
    q = [g[0]]  # 시작점 인큐
    v = [0]*(N+1)   # visited 생성
    v[g[0]] = 1     # 시작점 방문 표시
    cnt = 0
    while q:    # 정점이 남아있으면
        t = q.pop(0)
        cnt += 1
        for i in adjl[t]:
            if i in g and v[i]==0:
                q.append(i)
                v[i] = 1
    if len(g)==cnt:
        return 1
    else:
        return 0

N = int(input())
population = list(map(int, input().split()))
adjl = [[]] # 1번부터 N번까지 인접 리스트
for i in range(N):
    tmp = list(map(int, input().split()))
    adjl.append(tmp[1:])

arr = [i for i in range(1, N+1)]
min_v = 1000
for i in range(1, (1<<N)//2):
    A = []
    B = []
    pA = pB = 0
    for j in range(N):
        if i&(1<<j):
            A.append(arr[j])    # A 그룹에 속한 구역번호
            pA += population[j] # A 그룹의 인구 합계
        else:
            B.append(arr[j])
            pB += population[j]
    #print(A, B)
    r1 = f(A, N)
    r2 = f(B, N)
    if r1 and r2:       # A, B 둘 다 정상인 경우
        if min_v > abs(pA-pB):
            min_v = abs(pA-pB)
if min_v == 1000:   # 실패하는 경우
    min_v = -1
print(min_v)