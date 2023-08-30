'''
N개의 숫자
두 개의 집합으로 분류, 각 집합은 원소가 1개 이상
6
7 2 3 5 4 1
'''

N = int(input())
arr = list(map(int, input().split()))
for i in range(1, (1<<N) // 2):
    A = []
    B = []
    for j in range(N):
        if i & (1 << j):
            A.append(arr[j])
        else:
            B.append(arr[j])

    print(A, B) # indent 유의
