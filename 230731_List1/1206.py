# from sys import stdin as s
# s = open('input.txt', 'rt')
#
# for line in s:
#     print(s)

# for tc in range(1, 11):

T = 10
for tc in range(1, T + 1):
    summation = 0
    length = int(input())
    arr = list(map(int, input().split()))
    for i in range(length):
        jo = 0
        if arr[i] == 0: # 양 끝 제외
            continue
        if (arr[i - 1] < arr[i] and
                arr[i - 2] < arr[i] and
                arr[i + 1] < arr[i] and
                arr[i + 2] < arr[i]): # 양 옆 두칸 보다 해당 건물이 클 때
            jo = arr[i] - max(arr[i - 2], arr[i - 1], arr[i + 1], arr[i + 2])
            summation += jo

    print(f'#{tc} {summation}')