'''
열에서 하나만 고를 수 있도록 순열을 만든다.
'''

# def f(i,N):
#     global min_v
#     if i == N: # 끝까지 왔어
#         for p in range(N):
#             s += arr[p][A[p]]
#         if min_v > s:
#             min_v = s
#     else:
#         # 자리 바꾸기(자신부터 오른쪽 끝까지, 왼쪽으로 바꾸면 중복이됨)
#         for j in range(i, N):
#             A[i], A[j] = A[j], A[i]
#             f(i + 1, N)
#             A[i], A[j] = A[j], A[i] # 원상복구
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     A = [i for i in range(N)]
#     min_v = 100
#     f(0,N)
#     print(f'#{tc} {min_v}') # 전부 다 끝나면 전역변수인 min_v에 갱신된 최소값이 저장이 된단다.

'''
백트래킹 -> 어느 정도에서 최소값보다 같거나 크다면 더 이상 볼 필요가 없다.
'''

'''
합 까지 한 번에 함수에 넣기
'''

def f(i,N,s):
    global min_v
    if i == N: # 모든 행에서 선택이 끝난 경우 (잘 골랐구나?)
        if min_v > s:
            min_v = s
        return
    elif min_v < s: # 아직 더 선택해야 하는데 최소값보다 크다면 -> 뒤에 더 볼 필요가 없어 -> 더하면 더 커지는데 최소값 구해야 하니까 !
        return
    else:
        # 자리 바꾸기(자신부터 오른쪽 끝까지, 왼쪽으로 바꾸면 중복이됨)
        for j in range(i, N):
            A[i], A[j] = A[j], A[i]
            f(i + 1, N, s + arr[i][A[i]]) # 선택했음
            A[i], A[j] = A[j], A[i] # 원상복구

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    A = [i for i in range(N)]
    min_v = 100
    f(0,N,0)
    print(f'#{tc} {min_v}') # 전부 다 끝나면 전역변수인 min_v에 갱신된 최소값이 저장이 된단다.