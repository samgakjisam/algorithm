'''
1 이상 N2 이하의 수
이동하려는 방 숫자 = 현재 방 + 1
어디서부터 해야함?
'''
def f(i,j,num,cnt,k): #
    global max_v
    global max_start
    if j+1<N and arr[i][j+1] == num + 1: # 갈 수 있으면
        f(i,j+1,arr[i][j+1],cnt+1, k)
    elif i+1<N and arr[i+1][j] == num + 1: # 갈 수 있으면
        f(i+1,j,arr[i+1][j],cnt+1, k)
    elif j-1 >= 0 and arr[i][j-1] == num + 1: # 갈 수 있으면
        f(i,j-1,arr[i][j-1],cnt+1, k)
    elif i-1 >= 0 and arr[i-1][j] == num + 1: # 갈 수 있으면
        f(i-1,j,arr[i-1][j],cnt+1, k)
    else: # 갈 수 없으면
        if cnt > 1:
            if max_v <= cnt:
                max_v = cnt
                ans.append([k,max_v])

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    min_k = 0
    ans = []

    for i in range(N):
        for j in range(N):
            num = arr[i][j]
            # 출발하는 곳, 그곳의 수, 들린 방
            f(i,j,num,1,num)
    ans.sort(reverse=True)
    for i in range(len(ans)):
        if ans[i][1] == max_v:
            min_k = ans[i][0]
        else:
            pass

    print(f'#{tc} {min_k} {max_v}')
    # {min_k} {max_v}')