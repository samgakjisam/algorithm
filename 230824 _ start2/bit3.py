def ce(n): # change endian
    p = []
    for i in range(0, 4):
        p.append((n >> (24 - i*8)) & 0xff)
    return p

def ce1(n):
    return (n << 24 & 0xff000000) | (n << 8 & 0x00ff0000) | (n >> 8 & 0x0000ff00) | (n >> 24 & 0x000000ff)
    #        '04'를 맨 앞으로              '03'을 그 뒤로            '02'를 그 뒤로           '01'을 맨 앞으로
x = 0x01020304
p = []
for i in range(0,4):
    p.append((x >> (i * 8)) & 0xff)

print ('x = %02x%02x%02x%02x' % (p[0], p[1], p[2], p[3])) # %02x => 16진수 변환
p = ce(x)
print('x = %02x%02x%02x%02x' % (p[0],p[1],p[2],p[3]))

print(hex(ce1(x)))
