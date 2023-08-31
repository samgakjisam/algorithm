'''
N개의 컨테이너를 옮겨야 함
-> 각각 weight 있음
M대의 트럭이 있음
-> 각각 적재 용량이 있음

화물의 총 중량이 최대가 되도록 옮겨야 한다.


순열로 화물 N개 중 M개 뽑는다. (순서가 있어야 함)

화물을 싣지 못할 수도 있고, 남는 화물이 있을 수도 있다.

컨테이너 하나도 옮길 수 없을 때는 0을 출력한다.

'''

'''
일단 적재용량이 가장 큰 화물차에다가 큰 거부터 싣기
'''

T = int(input())

for tc in range(1, T + 1):
    N,M = map(int, input().split()) # 컨테이너, 트럭 수
    wei = list(map(int, input().split()))
    take = list(map(int, input().split()))

    wei.sort(reverse=True)
    take.sort(reverse=True)

    ans = 0
    i = 0
    j = 0
    while True:
        if i == M or j == N:
            break
        if take[i] < wei[j]: # 용량이 더 작으면
            j += 1 # 다음 화물
            continue
        if take[i] >= wei[j]: # i번 째 트럭의 용량이 j번 째 무게보다 크면
            ans += wei[j] # 담고
            i += 1 # 다음 트럭
            j += 1 # 다음 화물

    print(f'#{tc} {ans}')
