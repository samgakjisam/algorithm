T = int(input())

for tc in range(1, T + 1):
    gwaro = list(map(str, input()))

    stack = [0] * 100000
    top = -1
    cnt = 0

    for i in range(len(gwaro)):
        if gwaro[i - 1] == '(' and gwaro[i] == ')': # 레이저 잘린 거 표현
            cnt += top
        if top > -1 and gwaro[i] == ')':
            if gwaro[i - 1] == '(': # 괄호를 레이저로 인식하면
                cnt -= 1 # 막대기가 아니라서 빼줘야함
            top -= 1
        else:
            top += 1
            stack[top] = gwaro[i]
            cnt += 1 # 레이저 잘리기 전에 먼저 세줘야 더하면 답이 맞음

    print(f'#{tc} {cnt}')

