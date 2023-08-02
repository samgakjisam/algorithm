'''
같은 학년 같은 성별 같은 방
'''

N, K = map(int, input().split()) # 학생 수, 방 하나 최대 인원 수
# 성별 여/남 (0/1) , 학년
stu = [list(map(int, input().split())) for _ in range(N)]
man = []
woman = []
