def find_code(N, M):
    num_s = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3,
             '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7,
             '0110111': 8, '0001011': 9}

    for i in range(N):  # 세로 길이

        for j in range(M - 56 + 1):  # 몇 번째부터 시작?
            code=[]
            for p in range(0, 48, 8):  # 한 숫자의 시작 점
                temp = ''  # 7개 훑으면 초기화

                for k in range(7):  # 한 번 훑기
                    temp += arr[i][j + p + k]
                if temp in num_s:
                    code.append(num_s[temp])

                if len(code) == 8:
                    print(code)
                    sum = 0
                    for l in range(8):
                        if l % 2 == 0:
                           sum += int(code[l]) * 3
                        else:
                            sum += int(code[l])
                    if sum % 10 == 0:
                        print(sum)
                        return code



T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]
    # print(arr[0][0])
    print(find_code(N, M))
