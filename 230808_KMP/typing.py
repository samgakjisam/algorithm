T = int(input())

def getlps(pat):
    length = len(pat) # 패턴의 길이
    lps = [0] * length # lps 배열 선언
    j = 0
    for i in range(1, length):
        # 일치하지 않았을 때, lps배열의 j-1 값이 비교 인덱스로
        while j > 0 and pat[i] != pat[j]: # 다르면 while문 진입, j = 0이면 탈출
            j = lps[j - 1]
        if pat[i] == pat[j]: # 같으면 j 증가, j 값 lps i 번째 인덱스
            j += 1
            lps[i] = j
    return lps

def kmp(t,p):
    cnt = 0 # 키 누른 횟수
    lps = getlps(p)
    text_length = len(t)
    pattern_length = len(p)
    j = 0
    for i in range(text_length):
        while j > 0 and t[i] != p[j]: # 값이 매칭이 되지 않았을 때, lps[j-1] 값을 j 인덱스로
            j = lps[j - 1]
        if t[i] == p[j]:
            if j == (pattern_length - 1): # 전체 문자열 매칭
                cnt += 1 # 키 한 번 누르기 (패턴)
                j = lps[j] # 점프
                if t[i] == p[j]: # i += 1됐을 때 같으면
                    j = 0 # 비교 인덱스 초기화
            else:
                j += 1
    return cnt

for tc in range(1, T + 1):
    text, pattern = map(str, input().split())
    pat_cnt = kmp(text, pattern)
    ans = pat_cnt + (len(text) - len(pattern) * pat_cnt)

    print(f'#{tc} {ans}')