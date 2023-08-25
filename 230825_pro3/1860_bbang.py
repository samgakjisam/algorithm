T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())  # N명 / M초 -> K개
    second = list(map(int, input().split()))  # 각 사람의 도착 시간
    second.sort()  # 오름차순
    ans = 'Possible'
    cnt = 0

    for i in range(N):
        bbang = (second[i] // M) * K - cnt  # 빵 개수 (왔다간 사람이 산 거 포함)
        if bbang:  # 빵 있니?
            cnt += 1
        else:
            ans = 'Impossible'
            break

    print(f'#{tc} {ans}')