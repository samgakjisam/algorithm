# 4개의 직사각형이 주어진다. => 면적 구해라
# 겹칠 수도 있다. -> 합 집합을 구해야 한다.
# 각 줄은 왼쪽아래(x,y) 오른쪽위(x,y) 이다.

# for문 돌려서 1*1의 세트로 만들어서 집합 해버려?
# 가로세로 1씩 증가시키면 하나의 작은 요소

new_list = [] # 단위 사각형을 담을 리스트

def rec_area(lst):
    for i in range(lst[0], lst[2]):
        for j in range(lst[1], lst[3]):
            if [i, j, i + 1, j + 1] not in new_list: # 중복 제거
                new_list.append([i, j, i + 1, j + 1]) # 1*1 단위 정사각형 리스트에 추가

for _ in range(4):
    print("입력해,,,")
    rec_area(list(map(int, input().split())))

print(len(new_list)) # 중복을 제거한 사각형 합집합 넓이

## 언패킹 사용해볼까
new_list = [] # 단위 사각형을 담을 리스트

def rec_area(x1, y1, x2, y2):
    for i in range(x1, x2):
        for j in range(y1, y2):
            if [i, j, i + 1, j + 1] not in new_list: # 중복 제거
                new_list.append([i, j, i + 1, j + 1]) # 1*1 단위 정사각형 리스트에 추가

for _ in range(4):
    rec_area(*list(map(int, input().split())))

print(len(new_list)) # 중복을 제거한 사각형 합집합 넓이
