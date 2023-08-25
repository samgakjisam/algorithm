bit = [0] * 8
a = 149

i = 7
while a >= 2:
    bit[i] = a%2
    a //= 2
    i -= 1

# bit[i] = a
print(''.join(map(str,bit)))

