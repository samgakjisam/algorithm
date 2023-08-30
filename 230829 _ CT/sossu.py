'''
a이상 b이하인 정수 중 소수의 합
2<=a<=b<=1000000
T = 10만개.....
'''

def f(n):   # n 이 소수면 1 아니면 0을 리턴하는 함수, n>=2
    if n==2:    # n<=3
        return 1    # 2는 소수
    elif n%2==0:
        return 0
    else:
        i = 3
        while(i*i<=n):
            if n%i==0:
                return 0 # 약수가 있으므로 소수 아님
            i += 1
        return 1         # n**1/2까지 약수가 없으면 소수
# print(f(2))
# print(f(3))
# print(f(4))
# print(f(5))
# print(f(31))
# print(f(30))
# print(f(1000000007))

'''
a,b가 크고 TC가 많으면 시간이 오래걸림
'''
# a, b = map(int, input().split())
# s = 0
# for i in range(a, b+1):
#     if f(i):        # i가 소수인 경우
#         s += i
# print(s)

#인덱스 i가 소수인지 표시
prime = [0]*1000001
for i in range(2, 1000001):
    prime[i] = f(i)

# 에라토스테네스의 체....
arr = [1]*1000001
for i in range(2, 1000001):
    if arr[i]:  # i가 소수면
        j = 2
        while i*j<=1000000:
            arr[i*j] = 0
            j += 1
print(arr)