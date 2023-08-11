T = int(input())

for tc in range(1, T + 1):
    gwaro = list(map(str, input()))
    stack = []
    cnt = 0
    for i in range(len(gwaro)):
        if gwaro[i] == ')':
            if gwaro[i - 1] == '(': # 레이저
                cnt += len(stack) - 1 # 스택에 쌓인 수 더하기 [자르기]
                cnt -= 1 # 레이저면 막대기가 아님(스택 쌓을 때 cnt 올라간 거를 빼줘야 함[15번째 줄])
            stack.pop()
        else:
            stack.append(gwaro[i])
            cnt += 1 # 레이저 잘리기 전에 먼저 세줘야 됨

    print(f'#{tc} {cnt}')