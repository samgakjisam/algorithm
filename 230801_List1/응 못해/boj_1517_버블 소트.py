N = int(input())
A = list(map(int, input().split()))

# O(N^2)
cnt = 0

for i in range(N - 1, -1, -1): # 정렬한 수를 저장할 배열의 마지막 인덱스
    print(i)
    for j in range(i): # 마지막 인덱스인 i 전까지 비교
        if A[j + 1]<= A[j]:
            A[j], A[j + 1] = A[j + 1], A[j]

print(A) 
