def enq(data):
    global rear
    global front
    if (rear + 1) % N == front: # 가는 곳이 front와 동일하면
        front = (front + 1) % N # front도 한칸 옮겨준다.
    rear = (rear + 1) % N
    cqueue[rear] = data


def rotation(M):
    temp = 0
    for _ in range(M+1):
        temp = cqueue.pop(0)
        cqueue.append(temp)


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N:자연수 개수, M:작업 수
    arr = list(map(int, input().split()))  # 수열

    front = 0
    rear = 0
    cqueue = [0] * N

    for i in range(N):  # 큐에 자연수 N개 넣기
        enq(arr[i])
    rotation(M)
    print(f'#{tc} {cqueue[0]}')