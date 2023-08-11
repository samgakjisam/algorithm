T = int(input())

def find_hoemun(s, N, M):
    lps = [0] * N
    i = 1
    j = 0
    while i < N:
        if s[i] == s[j]: # 비교했을 때 같으면
            j += 1
            lps[i] += 1
            i += 1
        else: # 비교했을 때 다르면
            if j != 0: # 이전에 회문패턴 있을 경우
                j = lps[j - 1] # j 인덱스를 당겨온다 (스킵)
            else: # 이전에 회문 패턴 없으면
                lps[i] = 0
                i += 1

    return lps


for tc in range(1, T + 1):
    N, M = map(int, input().split()) # N x N , 길이가 M인 회문
    arr = [list(map(str, input().split())) for _ in range(N)] # 배열

    cnt = 0 # 회문 개수

    for k in range(N): # 행 탐색
        print(find_hoemun(*arr[k], N, M)) # 행 리스트 + 행 길이 + 회문 길이
    print('')