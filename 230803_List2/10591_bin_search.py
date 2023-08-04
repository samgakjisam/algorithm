T = int(input())

for tc in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())
    A = 0
    B = 0

    def binarySearch(N, key):
        l = 1
        r = N
        cnt = 0
        while l <= r:
            c = int((l + r)/2)
            cnt += 1
            if c == key:
                return cnt
            if c > key:
                r = c
            else:
                l = c

    A = binarySearch(P, Pa)
    B = binarySearch(P, Pb)

    if A < B:
        print(f'#{tc} A')
    elif A == B:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} B')