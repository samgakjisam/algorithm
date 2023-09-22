'''
union
find
'''
def find(x):
    if parents[x] == x: # 부모가 자기 자신이면
        return x
    else:
        # 경로 압축
        parents[x] = find(parents[x])
        return parents[x]

def union(x,y):
    a = find(x)
    b = find(y)

    # 사이클이 발생해도 됨
    if a == b:
        return
    # 최소값이 부모
    if a > b:
        parents[a] = b
    else:
        parents[b] = a

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    edge = [list(map(int, input().split())) for _ in range(M)] # 간선 정보
    parents = [i for i in range(N+1)] # 부모 정보

    for e in edge:
        union(e[0], e[1])

    for i in range(1, N+1):
        find(i)

    ans = len(set(parents)) - 1


    print(f'#{tc} {ans}')