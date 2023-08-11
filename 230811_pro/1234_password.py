T = 10

for tc in range(1, T + 1):
    N, M = map(str, input().split()) # 개수, 문자열
    N = int(N)

    stack = [0] * 100
    top = -1

    for ch in M:
        if top > -1 and stack[top] == ch: # 스택에 글자가 있고, 같은 문자이면
            top -= 1
        else: # 비어 있거나 다르면 stack
            top += 1
            stack[top] = ch

    print(f'#{tc}', end=' ')
    for i in range(top + 1):
        print(f'{stack[i]}', end='')
    print('')
