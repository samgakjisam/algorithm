def f(i,s,B):
    global min_v
    if s >= B:
        if min_v > s:
            min_v = s
        return
    if i == N:
        return
    else:
        f(i+1,s+H[i],B) # 선택함
        f(i+1,s,B) # 선택 안함

T = int(input())

for tc in range(1, T + 1):
    N, B = map(int, input().split()) # 점원 수, B 이상이여야 됨
    H = list(map(int, input().split()))

    min_v = int(1e9)

    f(0,0,B) # H 고르는 인덱스, 합, B는 목표

    print(f'#{tc} {min_v-B}')