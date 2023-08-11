T = int(input())

def push(item):
    global top
    top += 1
    stack[top] = item

def pop():
    global top
    top -= 1
    return stack[top + 1]

for tc in range(1, T + 1):
    s = list(input())
    stack = [0] * 100
    top = -1

    g = ['(', ')', '{', '}', '[', ']']

    for i in range(len(s)):
        if s[i] in g: # 괄호이면
            if stack[top] == g[0]: # '('
                if s[i] == g[1]: # 짝 맞으면
                    pop()
                else:
                    push(s[i])
            elif stack[top] == g[2]:  # '{'
                if s[i] == g[3]: # 짝 맞으면
                    pop()
                else:
                    push(s[i])
            elif stack[top] == g[4]:  # '['
                if s[i] == g[5]: # 짝 맞으면
                    pop()
                else:
                    push(s[i])
            else:
                push(s[i])

    print(f'#{tc}', end=' ')
    if top == -1:
        print(1)
    else:
        print(0)
