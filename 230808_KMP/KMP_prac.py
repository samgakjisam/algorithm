def kmp(txt, pat):
    M = len(txt)


def getlps(s):
    M = len(s)
    j = 0
    i = 1
    lps = [0] * M

    while i < M:
        if s[i] == s[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0: # 이전에 패턴이 있음
                j = lps[j - 1] # j 인덱스만 갱신해서 i는 그대로에다가 다시 비교
            else: # 없음 -> lps 0 하고 i 증가
                lps[i] = 0
                i += 1