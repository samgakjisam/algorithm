'''
순열로 풀어보기
- 순열 만들기
재귀함수 활용

'''
def check(p):
    global ans
    cnt = 0
    for i in range(0,6,3):
        if p[i] == p[i+1] and p[i+1] == p[i+2]: # 같은 수
            cnt += 1
        elif p[i] + 1 == p[i+1] and p[i+1] + 1 == p[i+2]: # 연속한 수
            cnt += 1
    if cnt == 2:
        ans = 'Baby Gin'
        return 1
    else:
        return 0

def perm(i,N):
    if i == N: # 6자리 다 채웠으면
        x = check(p) # 만들어진 배열이 baby-gin인지 확인
        return x
    else:
        for j in range(N): # 6자리 순회
            if used[j] == 0: # 사용되지 않았으면
                p[i] = num[j] # 순열에 넣기
                used[j] = 1
                if perm(i+1, N): # 다음자리로
                    return 1
                used[j] = 0 #풀어주기


T = int(input())
for tc in range(1, T + 1):
    N = 6 # 6자리 수
    num = list(map(int, input()))
    p = [0] * 6 # 순열을 넣을 배열
    used = [0] * 6 # 사용됐는지 여부
    ans = 'Lose'

    perm(0,N)
    print(f'#{tc} {ans}')