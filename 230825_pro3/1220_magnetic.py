'''
N극이면 True로 바꾸고 S이면 카운트세고 False로 다시 바꾸는 방법도 좋은거같다.
'''

T = 10

for tc in range(1, T + 1):
    a = int(input())  # 100
    arr = [list(map(int, input().split())) for _ in range(100)]

    cnt = 0

    # 0 없애기
    for i in range(a):
        temp = []
        for j in range(a):
            if arr[j][i] != 0:  # 0 아닌데
                if not temp and arr[j][i] == 2:  # 앞 2(S) 제거
                    continue
                else:
                    temp.append(arr[j][i])
        # 뒤 1(N) 제거
        while temp[-1] == 1:
            temp.pop()
        # 교착상태 카운트
        for k in range(len(temp) - 1):
            if temp[k] == 1 and temp[k + 1] == 2:
                cnt += 1

    print(f'#{tc} {cnt}')