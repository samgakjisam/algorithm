def f(i,N,K): # i:이전에 고른 개수, N개에서 K개를 고른 순열
    global cnt
    if i == K: # 순열 완성 : K개를 고른 경우
        cnt += 1
        print(cnt, p)
        return
    else:
        for j in range(N): # N개 중에서 고르기
            if used[j] == 0: # 사용되지 않았으면
                p[i] = card[j] # i 자리에 그 카드를 넣어
                used[j] = 1 # 사용되는 걸로 만들어
                f(i+1, N, K) # 다음 자리로
                used[j] = 0 # 다녀오면 풀어줄게

card = [1,2,3,4,5]
N = 5 # N개의 숫자에서
K = 3 # K개를 골라 만드는 순열
used = [0] * N # 사용한 카드
p = [0] * K
cnt = 0
f(0,N,K)