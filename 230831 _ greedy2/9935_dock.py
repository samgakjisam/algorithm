'''
최대한 많은 화물차
1. 종료 시간이 빠른 순서로 활동 정렬
2. 첫 번째 활동 선택
3. 선택한 활동의 종료시간보다 빠른 시작 시간을 가지는 활동을 모두 제거
4. 남은 활동들에 대해 앞의 과정 반복
'''

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    task = [[0,0] for _ in range(N)]
    for i in range(N):
        f,t = map(int,input().split())
        task[i][0] = f
        task[i][1] = t

    task.sort(key= lambda x:x[1]) # 시작시간 기준 오름차순

    task = [[0,0]] + task

    S = []
    j = 0
    for i in range(1, N+1):
        if task[i][0] >= task[j][1]: # 이전 끝 시간보다 지금 시작 시간이 크거나 같다면
            S.append(i) # 그 중에서 종료 시간 가장 빠른 것
            j = i # 변경

    print(f'#{tc} {len(S)}')