N = 10
a = [1,4,1,6,6,10,5,7,3,8,5,9,3,5,8,11,2,13,12,14]

meet = []
for i in range(N):
    meet.append([a[i*2], a[i*2+1]])
print(meet)
meet.sort(key=lambda x:x[1])
print(meet)
