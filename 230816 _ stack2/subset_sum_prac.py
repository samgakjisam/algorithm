def f(i, N, s, t): # s : i-1 원소까지 부분집합의 합(포함된 원소의 합), t: 찾으려는 합
    global cnt
    cnt += 1
    if s == t: # 합이 t인 경우
        print(bit)
        return
    elif i == N: # 남은 원소가 없는경우
        return
    elif s > t:
        return

    else:
        bit[i] = 1 # 부분집합에 A[i] 포함
        f(i + 1, N, s + A[i], 10) # 이전합에서 A[i]를 더함
        bit[i] = 0 # 부분집합에 A[i] 빠짐
        f(i + 1, N, s, 10) # 이전까지의 합과 같음
        return


# 1부터 10을 원소로 갖는 집합, 부분집합의 합이 10인 경우는?
N = 10
A = [i for i in range(1, N + 1)]
bit = [0] * N
cnt = 0
# f(0, N, 0)
# print(cnt) # f(0,N,0) 일 때 2047
f(0,N,0,10)
print(cnt) # f(0,N,0,10) 일 때 1701 => elif s > t: 조건 없을 때 -> 조건 생기면 349
# f(0,N,0,55)일 때는 최악의 조건이기 때문에 DFS와 동일하게 2047이다.