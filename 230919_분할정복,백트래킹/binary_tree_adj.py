def preorder(nodeNumber):
    if nodeNumber == None:
        return

    print(nodeNumber, end=' ') # 부모 먼저
    preorder(nodes[nodeNumber][0]) # 왼쪽부터
    preorder(nodes[nodeNumber][1]) # 오른쪽

arr = [1,2,1,3,2,4,3,5,3,6]


nodes = [[] for _ in range(0,14)]
for i in range(0, len(arr), 2):
    parentNode= arr[i]
    childNode = arr[i+1]
    nodes[parentNode].append(childNode)
    # nodes[childNode].append(parentNode) # 양방향 표시, 그래프에서는 필요하나 트리 구조에서는 필요없음 (자식 출발은 없음)

# 순회
# 자식이 더 이상 없다는 걸 표현하기 위해 None을 삽입
for li in nodes:
    for _ in range(len(li), 2):
        li.append(None)


for i in range(len(nodes)):
    print(nodes[i])

preorder(1)
