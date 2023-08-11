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
    txt = list(input())
    stack = [0] * 1000 # 길이가 1000이내인 문자열 -> 20으로 바꿨을 때 런타임 에러 발생
    top = -1
    for i in range(len(txt)):
        if txt[i] == stack[top]:
            pop()
        else:
            push(txt[i])

    print(f'#{tc} {top + 1}')