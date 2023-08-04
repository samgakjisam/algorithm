T = int(input())
arr = [i for i in range(1, 13)]
n = len(arr)

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    cnt = 0

    for i in range(1 << n):
        arr_b = [b for b in bin(i)]
        if arr_b.count('1') == N: # 원소 수 N개일 때
            i = int(''.join(arr_b), 2) # 문자열 -> 10진수
            subset = []
            for j in range(n):
                if i & (1 << j):
                    subset.append(arr[j])
            if sum(subset) == K:
                cnt += 1
    print(f'#{tc} {cnt}')