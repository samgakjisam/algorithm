'''
2를 곱한다.
10을 곱하고 1을 더한다.
'''
def f(a,b,c):
    global min_v
    if a == b:
        if min_v > c:
            min_v = c
        return
    if a > b:
        return
    if min_v < c:
        return
    else:
        f(a*2,b,c+1)
        f(a*10+1,b,c+1)


A, B = map(int, input().split())
min_v = 1e9

f(A,B,0) # A,B, 연산횟수

if min_v != 1e9:
    print(min_v+1)
else:
    print(-1)