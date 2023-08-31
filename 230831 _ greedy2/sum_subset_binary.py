A = [-1,3,-9,6,7,-6,1,5,4,-2]
N = len(A)

cnt = 0

for i in range(1, 1 << N): # 전체 부분집합의 수
    subset = []
    for j in range(N): # 이진수로 바꿨을 때 가능한 자리 수
        if i & (1 << j): # 포함
            subset.append(A[j])
    if sum(subset) == 0:
        cnt += 1

print(cnt)