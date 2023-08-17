def enq(data):
    global rear
    global front
    if (rear + 1) % cQsize == front: # rear가 front 이전
        # print('cQ is Full')
        front = (front + 1) % cQsize
    rear = (rear + 1) % cQsize
    cQ[rear] = data

    # else:
    #     cQ[rear] = data
    #     rear = (rear + 1) % cQsize


def deq():
    global front
    front = (front + 1) % cQsize
    return cQ[front]

cQsize = 4
cQ = [0] * cQsize
front = 0
rear = 0

enq(1)
print(cQ)
enq(2)
print(cQ)
enq(3)
print(cQ)
enq(4)
print(cQ)
enq(5)
print(cQ)

print(deq())
print(deq())

# def enq(data):
#     global rear
#     global front
#     if (rear + 1) % cQsize == front:
#         front = (front+1) % cQsize
#         print('cQ is Full')
#     else:
#         cQ[rear] = data
#         rear = (rear + 1) % cQsize
#
# def deq():
#     global front
#     front = (front + 1) % cQsize
#     return cQ[front]
#
# cQsize = 4
# cQ = [0] * cQsize
# front = 0
# rear = 0
#
# enq(1)
# print(cQ)
# enq(2)
# print(cQ)
# enq(3)
# print(cQ)
# enq(4)
# print(cQ)
# enq(5)
# print(cQ)
#
# print(deq())
# print(deq())
# print(deq())
# print(deq())
# print(deq())