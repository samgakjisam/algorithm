def getlps(s):
    M = len(s) # 문자열 길이
    lps = [0] * M # lps 배열
    j = 0
    i = 1 # 확인할 패턴 마지막 인덱스, 0은 걍 0이라 패스인듯
    while i < M: # 마지막 인덱스까지
        if s[i] == s[j]: # 같으면 i, j 같이 증가
            j += 1
            lps[i] = j # 최대 길이 갱신
            i += 1
        else: # 다르면 초기화
            if j != 0: # 이전까지 동일했으면
                j = lps[j - 1] # 이전까지의 동일한 길이를 건너뛴다.S
            else: # 처음부터 안맞으면
                lps[i] = 0 # 동일한 최대 길이는 0이다.
                i += 1
# i가 증가한다는 것은 A -> AB -> ABA ....
# j가 증가한다는 것은

    return lps

p = 'ABABABAC'
ans = getlps(p)
print(*ans)



# # 비교해서 다르면 while 탈출
# while s[i] != s[j] and j > 0:  # j > 0은 왜 있음
#     j = lps[j - 1]  # 이전 비교
#     print(j)
#
# if s[i] == s[j]:
#     lps[i] += j