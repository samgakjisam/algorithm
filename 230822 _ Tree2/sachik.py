'''
후위 순회로 연산
'''

def postorder(n):
    global result
    if tree[n] in '+-*/':
        if tree[n] == '+':
            return postorder(ch1[n]) + postorder(ch2[n])
        elif tree[n] == '-':
            return postorder(ch1[n]) - postorder(ch2[n])
        elif tree[n] == '*':
            return postorder(ch1[n]) * postorder(ch2[n])
        elif tree[n] == '/':
            return postorder(ch1[n]) // postorder(ch2[n])

    else:
        return tree[n]
T = 10

for tc in range(1, T + 1):
    N = int(input()) # 정점의 개수
    info = [list(map(str, input().split())) for _ in range(N)] # 트리 정보
    # 사칙 연산 혹은 숫자
    tree = [0] * (N + 1)

    # 사칙연산 기호만 ch1,2 존재
    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)

    for i in range(N):
        if info[i][1] in '+-*/': # 사칙 연산이면
            tree[int(info[i][0])] = info[i][1]
            ch1[int(info[i][0])] = int(info[i][2])
            ch2[int(info[i][0])] = int(info[i][3])
        else:
            tree[int(info[i][0])] = int(info[i][1])

     # 완전이진트리 root = 1
    print(f'#{tc} {postorder(1)}')


