'''
왼쪽 위와 마지막 # 찾고 좌표 저장
이후 변이 같은지 판별하고
중간에 # 아닌 게 없는 지 판별한다.
'''

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]

    check = []

    ans = 'no'

    for i in range(N):
        for j in range(N):
            if arr[i][j] == '#':
                x = i
                y = j
                if not check: # check에 아무것도 없으면
                    check.append([x,y]) # 첫 '#'을 check에 넣기

    check.append([x,y]) # 마지막 '#'
    x1, y1 = check[0]
    x2, y2 = check[1]

    flag = 0

    if x2 - x1 == y2 - y1:
        for i in range(x1, x2 + 1):
            if flag:
                break
            for j in range(y1, y2 + 1):
                if arr[i][j] == '.':
                    flag = 1
                    break
        else: # 다 돌면
            ans = 'yes'

    print(f'#{tc} {ans}')
