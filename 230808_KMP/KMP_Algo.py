def kmp(t, p):
    N = len(t)
    M = len(p)
    lps = [0] * (M + 1) # lps[0] = -1
    # lps값은 lps index의 접두 접미 패턴 같은 길이

    j = 0
    lps[0] = -1

    for i in range(1, M + 1):
        while




    for i in range(1, M):
        lps[i] = j
        if p[i] == p[j]:
            j += 1
        else:
            j = 0
    lps[M] = j



