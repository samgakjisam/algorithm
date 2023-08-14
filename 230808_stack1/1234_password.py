T = 10

def push(item):
    global top
    top += 1
    stack[top] = item

def pop():
    global top
    top -= 1
    return stack[top + 1]

for tc in range(1 ,T + 1):
    N, num = map(str, input().split())
    N = int(N)
    stack = [0] * N
    top = -1

    for i in range(N):
        if num[i] == stack[top]:
            pop()
        else:
            push(num[i])

    print(f'#{tc}', end=' ')
    for i in range(top + 1):
        print(stack[i],end='')
    print('')