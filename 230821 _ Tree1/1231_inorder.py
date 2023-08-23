'''
완전 이진 트리니까 루트가 1임
싹 다 안 차 있을 수도 있음 (n <= N)
'''

def inorder(n):
    if n <= N:
        inorder(n * 2)
        print(tree[n], end='')
        inorder(n * 2 + 1)

T = 10

for tc in range(1, T + 1):
    N = int(input()) # 트리가 갖는 정점의 총 수
    # 각각의 정점 정보
    info = [list(map(str, input().split())) for _ in range(N)]

    tree = [0] * (N + 1) # 트리 정보 넣을 리스트

    for i in range(N):
        tree[int(info[i][0])] = info[i][1]

    print(f'#{tc}', end= ' ')
    inorder(1) # 루트는 1이니까
    print()
