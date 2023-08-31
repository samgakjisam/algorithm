'''
교환은 무조건 해야함
교환할 카드를 2장 고르는 조합
'''
def cal(n,arr):
    cal = 0
    for p in range(n):
        cal += arr[p] * (10 ** (n - (p + 1)))
    return cal

def f(i,n,r,tr,s): # 트레이딩 횟수, nCr r: 뽑을 카드 수(2), 최대 교환 횟수
    global max_v
    if i == tr: # 트레이드 끝나면
        if max_v < s:
            max_v = s
        return
    if i >= 1 and arr[0] != max_c:
        return
    # if i >= 1 and (tr-i) % 2 == 0 and s >= max_v:
    #     max_v = s
    #     return
    if r == 0: # 다 뽑으면
        # 트레이드 하고
        arr[t_idx[0]], arr[t_idx[1]] = arr[t_idx[1]], arr[t_idx[0]]
        # 다음 트레이드
        f(i+1, N, 2, tr, cal(N,arr))
        arr[t_idx[0]], arr[t_idx[1]] = arr[t_idx[1]], arr[t_idx[0]]
        return
    if n < r: # 뽑을 카드 수보다 뽑힐 카드가 적을 경우 ( 더 이상 불가능 )
        return
    else: # 인덱스를 저장해서 처리
        t_idx[r-1] = n-1 # 인덱스 저장
        f(i,n-1,r-1,tr,s)
        f(i,n-1,r,tr,s)

T = int(input())

for tc in range(1, T + 1):
    K, tr = map(str, input().split()) # 최대 6자리 숫자, 교환 횟수

    tr = int(tr)
    N = len(K)
    arr = [int(K[i]) for i in range(N)]
    max_c = max(arr)
    t_idx = [0] * 2

    max_v = 0

    f(0,N,2,tr,0)
    print(f'#{tc} {max_v}')