'''
6528-*2/+
'''

stack = [0] * 100
top = -1
susik = '6528-*2/+'
for x in susik:
    if x not in '+-/*': # 피연산자이면...
        top += 1 # push(x)
        stack[top] = int(x)
    else:
        op1 = stack[top]  # pop()
        top -= 1
        op2 = stack[top]  # pop()
        top -= 1
        if x == '+': # op2 연산 op1 (스택에서 꺼낼 때는 반대이니까)
            top += 1
            stack[top] = op2 + op1
        elif x == '-':
            top += 1
            stack[top] = op2 - op1
        elif x == '/':
            top += 1
            stack[top] = op2 / op1
        elif x == '*':
            top += 1
            stack[top] = op2 * op1

    print(stack[top])