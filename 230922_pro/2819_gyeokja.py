'''
4x4 격자판, 0~9 숫자
상하좌우 6번 이동
이어 붙인다. -> 문자열 활용
한 번 거쳤던 격자판을 다시 거쳐도 된다. -> visited 필요 없음

완전탐색
'''
def f(i,j,n,s):
    if n == 7: # 1개 다 채우면
        m_list.append(s)
        return
    else:
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<4 and 0<=nj<4:
                f(ni,nj,n+1,s+arr[i][j]) # 선택

T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(str, input().split())) for _ in range(4)]
    s = ''
    m_list = []

    di = [0,1,0,-1]
    dj = [1,0,-1,0]

    for i in range(4):
        for j in range(4):
            f(i,j,0,s) # si,sj, 선택한 숫자
    ans = len(set(m_list))

    print(f'#{tc} {ans}')