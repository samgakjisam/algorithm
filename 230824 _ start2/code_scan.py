def find_code(N, M, step):
    num_s = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3,
             '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7,
             '0110111': 8, '0001011': 9}

    for i in range(N):  # 세로 길이

        for j in range(M - 56 * step + 1):  # 몇 번째부터 시작?
            code=[]
            for p in range(0, 49 * step + 1, 7 * step):  # 한 숫자의 시작 점
                temp = ''  # 8개 훑으면 초기화

                for k in range(7):  # 한 번 훑기
                    temp += arr[i][j + p + k]
                if temp in num_s:
                    code.append(num_s[temp])

                if len(code) == 8:
                    summation = 0

                    for l in range(7): # secret code
                        if l % 2 == 0: # hol
                           summation += int(code[l]) * 3
                        else: # zzak
                            summation += int(code[l])
                    summation += int(code[7])
                    if summation % 10 == 0:
                        return sum(code)

    return 0

def binary_change(arr):
    hex_info = {'A': 10, 'B': 11, 'C': 12, 'D': 13,
             'E': 14, 'F': 15}
    new_arr = []
    for i in range(N):
        temp_arr = []
        for j in range(M):
            temp = ''
            if arr[i][j] in hex_info: # >= 10
                temp = str(bin(hex_info[arr[i][j]])) # 0b00
                temp = temp[2:]
                for p in range(4): # 4 zari
                    temp_arr.append(temp[p])
            else:
                temp = bin(int(arr[i][j]))
                temp = temp[2:]
                if arr[i][j] != '8' or '9':
                    while len(temp) != 4:
                        temp = '0' + temp
                for p in range(4):  # 4 zari
                    temp_arr.append(temp[p])
        new_arr.append(temp_arr)
    return new_arr

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]
    x = binary_change(arr) # Hex => Bin

    for i in range(1,9): # 1~8
        if find_code(N,M,i):
            ans_lst.append(find_code(N, M, i))
        else:
            ans = 0

    print(f'#{tc} {ans}')