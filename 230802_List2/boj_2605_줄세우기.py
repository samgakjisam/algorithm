N = int(input()) # 학생 수
number = list(map(int, input().split())) # 뽑은 번호, 인덱스는 학생
result = [] # 뽑아서 정렬한 결과

def pick_number(stu_idx):
    result.insert(number[stu_idx], stu_idx + 1)
    # result.insert(stu_idx - number[stu_idx], stu_idx + 1)
    # 이거로 하면 역순으로 안나옴
    # 종이에 써보면 암
    

for i in range(N):
    pick_number(i)

real_result = result[::-1]

print(*real_result)