arr = [i for i in range(1, 13)]
n = len(arr)
subset = []
cnt = 0

for i in range(1 << n):  # 부분 집합의 개수
    for j in range(n):  # 원소의 수만큼 비트를 비교함
        if i & (1 << j):
            subset.append(arr[j])
    if sum(arr) == K:
        cnt += 1