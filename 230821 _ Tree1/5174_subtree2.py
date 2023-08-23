'''
노드 N을 루트로 하는 서브 트리에 속한 노드의 개수 알아내기
트리가 주어짐 -> 루트 찾기 -> 부모가 없는 녀석이 루트임
루트 찾고
후위 탐색 (타겟 노드에 관한 노드 개수 찾기 위해서) : LRV

### 자식 인덱스 부모 요소
'''

def postorder(n):
    global cnt
    if n: # 정점이 있으면
        postorder(ch1[n])
        postorder(ch2[n])
        cnt += 1

T = int(input())

for tc in range(1, T + 1):
    E, N = map(int, input().split()) # 간선, Target 노드
    info = list(map(int, input().split())) # E개의 부모 자식 노드 번호 쌍
    V = E + 1 # 정점의 개수
    root = 0 # 루트 숫자
    cnt = 0 # 노드 숫자 세기

    # 인덱스는 부모 번호
    ch1 = [0] * (V + 1) # 왼쪽
    ch2 = [0] * (V + 1) # 오른쪽

    for i in range(E): # 간선의 개수
        if ch1[info[i*2]] == 0: # 왼쪽 없으면
            ch1[info[i * 2]] = info[i * 2 + 1]
        else:
            ch2[info[i * 2]] = info[i * 2 + 1]

    # # 루트 찾기
    # # ch1, ch2의 요소로 한 번도 나오지 않은 숫자가 루트 숫자
    # f_root = [0] * (E + 2)
    # for i in range(E + 2):
    #     f_root[ch1[i]] += 1
    #     f_root[ch2[i]] += 1
    # for i in range(E + 2):
    #     if f_root[i] == 0:
    #         root = i
    # print(root)

    postorder(N)
    print(f'#{tc} {cnt}')