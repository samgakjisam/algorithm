# 모든 경우의 수를 나열해보고 확인하는 기법이다. (Brute-force)

A = list(map(int, input().split())) # 입력배열
counts = [0] * (max(A) + 1) # 카운트 배열
temp = [] # 정렬된 배열

for i in range(0, len(A)):
    counts[A[i]] += 1

for i in range(1, len(counts)):
    counts[i] += counts[i-1]

for i in range(len(temp) - 1, -1, -1):




