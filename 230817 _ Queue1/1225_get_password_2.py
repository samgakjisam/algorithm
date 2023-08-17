'''
원형 큐에서 사이즈를 하나 더 늘리는 이유는
큐가 가득찼을 경우 이후 처리를 해줘야 하기 때문이다.
'''

def enq(data):
    global rear
    rear = (rear + 1) % length
    qq[rear] = data

def deq():
    global front
    front = (front + 1) % length
    return qq[front]

def dodo(): # 감소시켜서 뒤로 이동
    global flag
    temp = 0
    for i in range(1, 6):
        temp = deq()
        temp -= i
        if temp <= 0: # 0보다 작으면
            flag = 0 # while문 탈출하기
            temp = 0
            enq(temp)
            return
        else:
            enq(temp)

T = 10

for tc in range(1, T + 1):
    x = int(input()) # tc 번호
    length = 8
    num = list(map(int, input().split())) # 8개의 숫자
    qq = [0] * length

    front = 0
    rear = 0

    flag = 1 # 반복 끝내기

    for i in range(length):
        enq(num[i])

    while flag:
        dodo()
    print(f'#{x}',end=' ')
    for _ in range(length):
        print(deq(), end= ' ')
    print('')