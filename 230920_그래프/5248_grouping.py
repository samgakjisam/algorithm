def find_set(x):
    if parent[x] == x:
        return x
    parent[x] = find_set(parent[x])
    return parent[x]


def union(a,b):
    a = find_set(a)
    b = find_set(b)
    # 작은 수가 부모가 되야 함
    if a == b:
        return

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int , input().split())
    parent =  [0] + [i+1 for i in range(N)]
    info = list(map(int,input().split()))
    for i in range(M):
        union(info[i*2], info[i*2+1])
    for i in range(1,N+1):
        find_set(i)


    ans = len(list(set(parent))) - 1
    print(f'#{tc} {ans}')