def enq(data): # 피자 초기에 넣기
    global rear
    global front
    if (rear + 1) % N == front: # 맨 처음 들어간 거 한 바퀴 돈거임?
        # if not isfull():
        front = (front + 1) % N
    rear = (rear + 1) % N
    hwaduck[rear] = data

def rotation():
    global front
    global rear
    front = (front + 1) % N
    rear = (rear + 1) % N
    melting(rear)

def melting(rear):
    hwaduck[rear][0] = hwaduck[rear][0] // 2 # 녹는다

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split()) # N: 화덕 크기, M: 피자 개수
    pizza = list(map(int, input().split())) # 치즈, M개 요소

    hwaduck = [[0,0] for _ in range(N)] # 화덕 = 원형큐
    front = 0
    rear = 0
    cnt = 0

    for i in range(N): # 피자 초기에 넣기
        enq([pizza[i], i]) # 인덱스까지 돌리기?

    last_index = N
    flag = 1

    while flag:
        # 계속 돌린다.
        rotation()
        if hwaduck[rear][0] == 0: # 다 녹으면
            if last_index < M: # 피자 바꾸기
                front = (front + (N-1)) % N # 뒤로
                rear = (rear + (N-1)) % N # 뒤로
                enq([pizza[last_index], last_index])
                last_index += 1
            else: # 꺼내기
                hwaduck[rear][1] = 0
        if last_index == M: # 피자 다씀
            cnt = 0
            for i in range(N):
                if hwaduck[i][0] == 0:
                    cnt += 1
                if cnt == N - 1:
                    flag = 0

    print(f'#{tc}', end=' ')
    for i in range(N):
        if hwaduck[i][0] != 0:
            print(hwaduck[i][1] + 1) # 인덱스 수정