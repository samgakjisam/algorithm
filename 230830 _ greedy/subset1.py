# arr = [3,6,7,1,5,4]
# N = 6
#
#
#
# for i in range(1<<N): # 모든 부분집합을 만드는 경우
#     subset1 = [] # 초기화 위치 생각
#     subset2 = []
#     for j in range(N):
#         if i & (1 << j): # j번 비트가 1이면
#             subset1.append(arr[j])
#         else:
#             subset2.append(arr[j])
#     print(subset1, subset2)

'''
두 개로 집합을 나눌 때에는 공집합이 있으면 안되고
중복이 되어서도 안된다.
'''
arr = [3,6,7,1,5,4]
N = 6


# 1부터 시작해서 공집합 제외
# 반만 해서 중복 제외 (1 << N) // 2 == 1 << (N-1) -> 2를 덜 곱한 것이니까
for i in range(1, (1<<N) // 2): # 모든 부분집합을 만드는 경우
    group1 = [] # 초기화 위치 생각
    group2 = []
    for j in range(N):
        if i & (1 << j): # j번 비트가 1이면
            group1.append(arr[j])
        else:
            group2.append(arr[j])
    print(group1, group2)
