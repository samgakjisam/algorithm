T = int(input())

for tc in range(1, T + 1):
    N = int(input()) # 사각형 개수
    arr = [list(map(int, input().split())) for _ in range(N)]  # 5번 째 인덱스는 색깔
    cnt = 0
    k = 0
    while k < (N - 1):
        for i in range(arr[k][0], (arr[k][2] + 1)): # 첫 번째 사각형 행 탐색
            for j in range(arr[k][1], (arr[k][3] + 1)): # 첫 번째 사각형 열 탐색
                for idx in range(k+1, N): # 다음부터 마지막 사각형까지 확인
                    if arr[k][4] != arr[idx][4]:  # 다음 사각형과 색깔이 다를 때
                        if arr[idx][0] <= i <= arr[idx][2] and arr[idx][1] <= j <= arr[idx][3]:
                            cnt += 1
        k += 1

    print(f'#{tc} {cnt}')