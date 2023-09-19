# 이진 검색 - 재귀호출 활용

arr = [2,4,7,9,11,19,23]

# 문제에서 데이터가 정렬되어 있다 라는 조건이 없다면
# 반드시 정렬을 먼저 수행해야 한다.
arr.sort()

def binarySearch(low, high, target):
    # 기저 조건 : 언제까지 재귀호출을 반복할 것인가?
    # low > high 라면 데이터를 못찾음
    if low > high:
        return -1

    mid = (low + high) // 2
    # 1. 가운데 값이 정답인 경우
    if arr[mid] == target:
        return mid
    # 2. 가운데 값이 정답보다 작은 경우
    elif arr[mid] < target:
        # 뒤 쪽으로 mid를 이동시킨다 (오른쪽에 답이 있다는 거니까)
        return binarySearch(mid+1, high, target)
    # 3. 가운데 값이 정답보다 큰 경우 (왼쪽 검색)
    else:
        return binarySearch(low, mid - 1, target)


print(f'9 = {binarySearch(0,len(arr)-1,9)}')
print(f'4 = {binarySearch(0,len(arr)-1,4)}')
print(f'19 = {binarySearch(0,len(arr)-1,10)}')