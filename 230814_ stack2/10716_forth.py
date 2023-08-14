'''
후위 연산자 -> 괄호가 없다.
'''

T = int(input())

for tc in range(1, T + 1):
    stack = [0] * 256
    top = -1

    forth = list(map(str, input().split()))

    for x in forth:
        # 피연산자이면
        if x == '.': # 연산 끝
            if top == 0:
                break
            else:
                stack[0] = 'error'
                break
        #     stack[0] = 'error'
        #     break
        # if top == 1:  # 연산 끝났는데도 결과 2개
        #     stack[0] = 'error'
        if x not in '+-/*':
            top += 1
            stack[top] = int(x)
        else: # 연산자이면
            # op2 (연산자) op1
            if top <= 0:
                stack[0] = 'error'
                break
            op1 = stack[top] # pop
            top -= 1
            op2 = stack[top] # pop
            top -= 1
            if x == '+':
                top += 1
                stack[top] = op2 + op1
            elif x == '-':
                top += 1
                stack[top] = op2 - op1
            elif x == '*':
                top += 1
                stack[top] = op2 * op1
            elif x == '/':
                top += 1
                stack[top] = op2 // op1


    print(f'#{tc} {stack[0]}')