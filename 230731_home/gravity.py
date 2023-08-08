# Gravity

T = int(input())

for tc in range(1, T + 1):
    width = int(input())
    height = list(map(int, input().split()))
    max_cnt = 0 # 최대 낙차
    max_temp = 0
    for i in range(len(height)):
        if max_temp > max_cnt: # 순회한 결과가 크다면
            max_cnt = max_temp # max 낙차 값 갱신
        max_temp = 0 # i가 리스트를 순회할 때 마다 초기화
        for j in range(i + 1, len(height)):
            if height[i] <= height[j]:
                continue
            elif height[i] > height[j]:
                max_temp += 1
    
    print(f'#{tc} {max_cnt}')       


        


