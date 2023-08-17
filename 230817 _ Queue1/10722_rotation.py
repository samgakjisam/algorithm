def enq(data):
    global rear

    rear += 1
    queue[rear] = data

def rotation(M):
    temp = 0
    for _ in range(M):
        temp = queue.pop(front + 1)
        queue.append(temp)


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split()) # N:자연수 개수, M:작업 수
    arr = list(map(int, input().split())) # 수열

    front = -1
    rear = -1
    queue = [0] * N


    for i in range(N): # 큐에 자연수 N개 넣기
        enq(arr[i])

    rotation(M)
    print(f'#{tc} {queue[0]}')