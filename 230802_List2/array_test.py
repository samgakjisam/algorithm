N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

total1 = 0 # 왼쪽위에서 오른쪽아래로 대각선 합
total2 = 0 # 오른쪽위에서 왼쪽아래로 대각선 합
for i in range(N):
    total1 += arr[i][i]

for i in range(N):
    total2 += arr[i][N - 1 - i] # i, j 의 합이 N이 되어야 함

print(total1, total2)