def enq(data):
    global rear
    rear += 1
    qq[rear] = data

def dodo(): # 감소시켜서 뒤로 이동
    global flag
    temp = 0
    for i in range(1, 6):
        temp = qq.pop(0)
        temp -= i
        if temp <= 0: # 0보다 작으면
            flag = 0
            temp = 0
            qq.append(temp)
            return
        else:
            qq.append(temp)

T = 10

for tc in range(1, T + 1):
    x = int(input()) # tc 번호
    length = 8
    num = list(map(int, input().split())) # 8개의 숫자
    qq = [0] * length
    ans = [0] * 10

    front = -1
    rear = -1

    flag = 1 # 반복 끝내기

    for i in range(length):
        enq(num[i])

    while flag:
        dodo()
    print(f'#{tc}',*qq)
