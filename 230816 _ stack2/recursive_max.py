def f(i,j): # A[i:j+1]에서 최댓값을 리턴하는 함수
    if i == j:
        return A[i]
    else:
        m = (i+j)//2 # 중간 인덱스
        r1 = f(i, m) # 왼쪽 최댓값
        r2 = f(m+1, j) # 오른쪽 최댓값
        return max(r1,r2)

A = [2,1,9,7,4,3]
N = len(A)
print(f(0,N-1))