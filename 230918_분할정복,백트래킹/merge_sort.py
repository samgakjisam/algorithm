# 재귀
# def merge_sort(m):
    # if len(m) == 1:
    #     return m
    # middle = len(m) // 2
    # # 데이터가 커지면 메모리 사용량이 급격하게 늘어난다.
    # # 리스트를 새로 만들지 말고 인덱스를 인자로 넘겨준다.
    # # start == end이면 기저 조건
    # left = [0:middle]
    # right = [middle:]
    # merge_sort(left)
    # merge_sort(right)

# 병합
def merge(l,mid,r):
    global cnt
    if arr[mid-1] > arr[r]:
        cnt += 1
    left = l # 왼쪽 구간의 비교위치, l 왼쪽 구간의 첫 원소 인덱스
    right = mid # 오른쪽 구간의 비교위치, mid+1 첫 원소 인덱스
    tidx = 0
    while left <= mid-1 or right <= r: # 아직 원소가 남아있으면
        if left <= mid-1 and right <= r:
            if arr[left] > arr[right]:
                temp[tidx] = arr[right]
                right += 1
            else: # 왼쪽 애가 더 작으면
                temp[tidx] = arr[left]
                left += 1
        elif left <= mid-1: # 왼쪽 구간만 원소가 남아있으면
            temp[tidx] = arr[left]
            left += 1
        else: # 오른쪽 구간의 원소만 남아있는 경우우
            temp[tidx] = arr[right]
            right += 1
        tidx += 1


    # 임시로 저장한 데이터를 적용
    for i in range(tidx):
        arr[l+i] = temp[i]


# 분할
def merge_sort(l,r): # l은 정렬 범위 시작, r은 정렬 범위 끝
    if l == r: # 원소가 1개인 경우
        return
    mid = (l+r+1)//2
    x = (l+r+1) // 2
    merge_sort(l,mid-1)
    merge_sort(mid,r)
    merge(l,mid,r)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    temp = [0] * N
    merge_sort(0,N-1) # 인덱스를 넘겨주기기
    print(f'#{tc} {arr[N//2]} {cnt}')