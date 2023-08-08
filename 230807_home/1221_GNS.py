T = int(input())

for tc in range(1, T + 1):
    tc_num, length = list(map(str, input().split()))
    length = int(length)
    arr = list(map(str, input().split()))
    number = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    cnt_arr = [0] * 10 # 0부터 9까지 숫자

    for i in range(length):
        for j in range(10):
            if arr[i] == number[j]:
                cnt_arr[j] += 1
                continue

    print(f'#{tc}')
    for i in range(10):
        print(f'{number[i]} ' * cnt_arr[i], end='')
        print('')
    print('')