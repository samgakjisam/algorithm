def f(i, N):
    if i == N: # 순열 완성
        print(p) # 처리
        return
    else: # p[i]에 들어갈 숫자를 결정

        for j in range(N):
            if used[j] == 0: # 아직 사용되지 않으면
                p[i] = card[j]
                used[j] = 1 # 사용됐음
                f(i+1, N) # 다음 자리로 이동
                used[j] = 0 # 갔다오면 풀어줄게

card = list(map(int, input()))
used = [0] * 6 # 이미 사용한 카드인지 표시
p = [0] * 6
f(0,6)