'''
복도 번호
짝수 // 2 , 홀수 + 1 // 2

복도 번호를 지나는 사람 수 카운트

최대값 찾기
'''

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    bokdo = [0] * 201 # 1 ~ 200번까지

    for a,b in arr:
        a = (a + (a % 2)) // 2 # a%2 홀수면 1임
        b = (b + (b % 2)) // 2
        for i in range(min(a,b), max(a,b) + 1):
            bokdo[i] +=1


    print(f'#{tc} {max(bokdo)}')