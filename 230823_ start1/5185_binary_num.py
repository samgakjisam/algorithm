def binary(n):
    output = ''
    for j in range(3,-1,-1):
        output += '1' if n & (1 << j) else '0'
    return output

T = int(input())

for tc in range(1, T + 1):
    N, my_hex = input().split()
    N = int(N)
    ans = ''
    hex_t = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    for i in range(N):
        if my_hex[i] in hex_t:
            ans += binary(hex_t[my_hex[i]])
        else:
            ans += binary(int(my_hex[i]))

    print(f'#{tc} {ans}')