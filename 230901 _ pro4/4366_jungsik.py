'''
3진수 0,1,2
2진수 0,1

1. 2진수 확인하고 3진수 바꾸면서 같은 값이 있는지 확인
2. 바꾸고 싶은 자리수에 1과 XOR 연산을 하면 그 자리만 변함
3. 3진수는 나머지 연산 활용
'''

T = int(input())
for tc in range(1, T + 1):
    A = input()
    B = list(map(int, input())) # 한칸씩 받기

    N = len(A)
    M = len(B)
    ans = 0

    binary = int(A, 2) # 이진수 형태
    bin_list = [0] * N # 각 비트를 반전시킨 수 N개 저장
    for i in range(N):# 각 비트를 반전시킨 2진수 만들기...
        bin_list[i] = binary ^ (1<<i) # i번 비트를 XOR 연산을 통해 반전시킴

    for i in range(M): # 3진수 i 자리를 변경
        num1 = 0 # (B[i] + 1) % 3
        num2 = 0 # (B[i] + 2) % 3
        for j in range(M):
            if i != j: # 바꿀 자리가 아니면
                num1 = num1 * 3 + B[j]
                num2 = num2 * 3 + B[j]
            else:
                num1 = num1 * 3 + (B[j] + 1) % 3
                num2 = num2 * 3 + (B[j] + 2) % 3
        if num1 in bin_list:
            ans = num1
            break # for i를 빠져나감
        if num2 in bin_list:
            ans = num2
            break

    print(f'#{tc} {ans}')