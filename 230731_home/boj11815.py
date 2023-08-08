# # from sys import stdin as s
# # s = open('input.txt', 'rt')
# '''
# 보통 약수는 소수이다.
# '''

# ### 시간초과

# N = int(input()) # 전체 테스트 개수
# X = list(map(int, input().split()))
# for i in range(N):
#     V = X[i] # 약수 개수를 판별할 수
#     cnt = 0 # 약수의 개수를 카운팅
#     for j in range(1, V + 1):  # 1부터 X 자신까지 순회
#         if V % j == 0:
#             cnt += 1
#     if cnt % 2 == 0:
#         print(f'0', end=' ')
#     elif cnt % 2 == 1:
#         print(f'1', end=' ')

### 숫자의 성질로 가자 ex) 2^2 * 3^2 = 36 => 약수 3 * 3 개
### Hint
### 어떤 특정한 수들의 종류의 약수가 홀수인지 짝수인지 생각해보는 것이 좋을 것 같습니다.
### ex) 소수의 약수는 전부 1과 자신 둘뿐입니다.
### => 홀수이려면 짝 * 짝 => 제곱수, 네제곱수 .... 어쨌든 root 씌우면 정수가 나옴(isinteger활용)
### ==> 틀림...
### 찾아보니까 부동소수점의 오류라고함. (정확히 왜 인지는 모르겠음)
### 남의 풀이 참고 (제곱근했다가 다시 제곱한게 원래 값과 같으면 제곱수)
N = int(input()) # 전체 테스트 개수
X = list(map(int, input().split()))

for i in range(N):
    if (X[i] == int(X[i] ** 0.5) ** 2): # 제곱수이면
        print(f'1 ', end='') # 약수는 홀수개
    else:
        print(f'0')
        

N = int(input()) # 전체 테스트 개수
X = list(map(int, input().split()))

for i in range(N):
    if (X[i] == int(X[i] ** 0.5) ** 2): # 제곱수이면
        print(f'1 ', end='') # 약수는 홀수개
    else:
        print(f'0')

## 남의 풀이   
# count = int(input())
# num = input()
# num = num.split()
# num = list(map(int, num))

# for i in range(count):
#     if num[i] == (int(num[i] ** 0.5) ** 2):
#         print(1, end = " ")
#     else:
#         print(0, end = " ")
        

