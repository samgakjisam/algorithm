def subset():
    for i in range(1<<N):


T = int(input())

for tc in range(1, T + 1):
    N, L = map(int, input().split()) # 재료 수, 칼로리 제한
    arr = [list(map(int, input().split())) for _ in range(N)]
    # [재료][0] : 점수 [재료][1] : 칼로리

    # 순서는 고려하지 않으므로 조합으로 간다. x -> 개수의 제한이 없기 때문에
    # 부분집합으로 가야함
    subset()