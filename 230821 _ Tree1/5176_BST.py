'''
- 완전 이진 트리는 루트 1이고 순서대로 차 있다.
- 포화는 레벨의 노드가 모두 차 있어야 하지만 완전은 상관없이 순서대로 다 차 있으면 된다.
ex 이 문제 그림에서 5번이 오른쪽에 있으므는 안된다.
- 루트는 부모가 없는 녀석
- 원래는 루트를 먼저 구해서 함수의 인자로 사용해야 하지만
  완전 이진 트리이므로 루트는 1이다.
- 처리를 할 때 값을 삽입해야지 -> LVR : 중위순회
- 왼쪽 서브트리의 루트 < 현재 노드 <오른쪽 서브 트리의 루트
'''

def inorder(n):
    global cnt # 1부터 저장할거임
    if n <= N: # N보다 작을 때
        inorder(n * 2)
        tree[n] = cnt
        cnt += 1
        inorder(n * 2 + 1)
    # return r, t


T = int(input())

for tc in range(1, T + 1):
    N = int(input()) # 1 ~ N까지의 자연수
    tree = [0] * (N+1) # 0 ~ N까지가 인덱스인 리스트

    target = N // 2
    cnt = 1 # 저장할 값 1부터 시작

    inorder(1)
    print(f'#{tc} {tree[1]} {tree[N // 2]}')