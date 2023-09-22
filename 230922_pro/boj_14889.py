'''
조합 -> 선택, 안선택
13%에서 틀림

만일 스타트팀에 [1, 3, 5, 7], 링크팀에 [2, 4, 6, 8] 이 들어있다고 하면 이 코드는 능력치 계산을 인접한 선수끼리만 하고 있습니다.

문제에서 요구하는 것은 팀 내의 모든 선수 조합에 대한 능력치 합입니다. (예를 들어, 위 스타트팀의 3번선수와 7번선수에 대한 능력치를 이 코드에서는 고려하지 않고 있습니다.)

N개 중에서 r개를 선택하는 조합
비트마스킹으로도 가능
'''

def comb(i,r,s,l):
    global min_v
    if len(l) > r//2 or len(s) > r // 2:
        return
    if i == r:
        start_sum = 0
        link_sum = 0
        # 인접한 친구들만 계산했슴
        for j in range(r//2):
            for k in range(r//2):
                if j != k:
                    start_sum += S[s[j]][s[k]]
        for j in range(r // 2):
            for k in range(r // 2):
                if j != k:
                    link_sum += S[l[j]][l[k]]

        a = abs(link_sum-start_sum)

        if min_v > a:
            min_v = a
        return
    else:
        s.append(i)
        comb(i+1,r,s,l)
        s.pop()
        l.append(i)
        comb(i+1,r,s,l)
        l.pop()

N = int(input()) # 짝수
S = [list(map(int, input().split())) for _ in range(N)]

st = []
li = []

min_v = 1e9

comb(0,N,st,li) # 시작, 반, 스타트, 링크

print(min_v)