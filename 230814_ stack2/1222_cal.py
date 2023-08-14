T = 10

for tc in range(1, T + 1):
    stack = [0] * 1000
    top = -1
    icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}  # 우선순위
    isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}  # 우선순위
    N = int(input())
    fx = map(str, input())
    susik = ''
    for x in fx:
        if x not in '(+-*/)':  # 피연산자
            susik += x ####
        elif x == ')':  # '('까지 pop()
            while stack[top] != '(':  # peek
                susik += stack[top] ###########
                top -= 1
            top -= 1  # '(' 버림. pop
        else:  # '(+-*/'
            if top == -1 or isp[stack[top]] < icp[x]:  # 토큰의 우선순위가 더 높으면
                top += 1  # push
                stack[top] = x ###############
            elif isp[stack[top]] >= icp[x]:
                while top > -1 and isp[stack[top]] >= icp[x]:
                    susik += stack[top]
                    top -= 1
                top += 1  # push
                stack[top] = x
    susik += stack.pop(0)
    stack2 = []
    for x in susik:
        # 피연산자이면
        if x not in '+-/*':
            stack2.append(int(x))
        else: # 연산자이면
            # op2 (연산자) op1
            op1 = stack2.pop()
            op2 = stack2.pop() # pop
            top -= 1
            if x == '+':
                stack2.append(op2 + op1)
            elif x == '-':
                stack2.append(op2 - op1)
            elif x == '*':
                stack2.append(op2 * op1)
            elif x == '/':
                stack2.append(op2 // op1)

    print(f'#{tc} {stack2[0]}')