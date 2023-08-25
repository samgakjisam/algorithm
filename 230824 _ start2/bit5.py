def Bbit_print(i):
    output = ''
    for j in range(7,-1,-1):
        output += '1' if i & (1 << j) else '0'
    print(output)

a = 0x86
key = 0xBB

print('a        ==> ', end='')
Bbit_print(a)
print('a^=key   ==> ', end='')
a ^= key
Bbit_print(a)
print('a^=key   ==> ', end='')
a ^= key
Bbit_print(a)

# XOR 연산을 활용 -> XOR 연산 두 번 하면 똑같은 숫자가 나온다.