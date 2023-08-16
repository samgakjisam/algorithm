'''
1은 가위, 2는 바위, 3은 보
'''

def f(i,j): # A[i:j+1]에서 최댓값을 리턴하는 함수
    if i == j:
        return i
    else:
        m = (i+j)//2 # 중간 인덱스
        r1 = f(i, m) # 왼쪽 최댓값
        r2 = f(m+1, j) # 오른쪽 최댓값
        return winner(r1, r2)

def winner(r1, r2):
    win = [[1, 2], [2, 3], [3, 1]]
    if [[card[r1], card[r2]]] in win:
        return r2
    else:
        return r1


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    card = list(map(int, input().split()))

    print(f'#{tc} {f(0,N-1)}')