'''
위치는 꼭지점이 될 수 없다.
반대로 생각해야 하니까 북 <-> 남
'''

ga, se = map(int, input().split()) # 5, 10일 경우 인덱스는 0~5, 0~10

block = [[0] * (ga+1) for _ in range(se+1)]

store = int(input())

start = 0

for i in range(store+1):
    bang, leng = map(int, input().split())
    if i == 0:
        K = 'D'
    else:
        K = i
    if bang == 1: # 북
        block[se][leng] = K
        if i == 0:
            start = [se,leng]
    if bang == 2: # 남
        block[0][leng] = K
        if i == 0:
            start = [0,leng]
    if bang == 3: # 서
        block[leng][0] = K
        if i == 0:
            start = [leng,0]
    if bang == 4: # 동
        block[leng][ga] = K
        if i == 0:
            start = [leng,ga]
print(start)

'''
동근이 있는 곳에서 일단 가보고 만나는 곳의 거리를 배열에 append
배열에서 그 인덱스의 최소값 찾아서 합 출력
'''

# # 시계방향
# clk()
# # 반시계방향
# clkw()
