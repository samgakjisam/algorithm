stack = [0] * 10 # 배열 size 결정
top = -1 # top 초기화

top += 1            # push(1)
stack[top] = 1
top += 1            # push(2)
stack[top] = 2
top += 1            # push(3)
stack[top] = 3

print(stack[top])   # pop()
top -= 1
top -= 1
print(stack[top + 1])