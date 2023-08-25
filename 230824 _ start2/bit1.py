def Bbit_print(i):
    output = ''
    for j in range(7,-1,-1):
        output += '1' if i & (1 << j) else '0'
    print(output)

for i in range(-5, 6):
    print('%3d =' %i, end='') # 음수 양수 자리 수 맞춰주기위해 %3d
    Bbit_print(i) # 음수는 2의 보수로 표현된다.