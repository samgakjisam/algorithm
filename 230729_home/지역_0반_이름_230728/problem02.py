def test(n):
    # lst = [] # 새로운 리스트 생성
    # for i in range(1, n+1): # 1부터, 30까지 순회
    #     if i % 2 == 1: # 홀수이면
    #         lst.append(i) # lst에 요소로 추가
    
    # 2. 리스트 컴프리헨션 활용
    lst = [i for i in range(1, n + 1) if i % 2 == 1] # 리스트 컴프리헨션은 리스트로 묶어줘야한다.
    
    return lst # 홀수로 이루어진 lst 반환

# 이 부분 수정 금지
n = 30
print(test(n))