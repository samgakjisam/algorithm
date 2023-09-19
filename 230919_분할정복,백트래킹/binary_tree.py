# 0. 이진 트리 저장
#       - 일차원 배열 저장
# 1. 연결 리스트로 저장
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # 삽입 함수
    def insert(self, childNode):
        # 왼쪽 자식이 없을 경우
        if not self.left:
            self.left = childNode
            return

        # 오른쪽 자식이 없을 경우
        if not self.right:
            self.right = childNode
            return

        # 다 없으면 걍 리턴
        return

    # 전위 순회 (부좌우)
    def preorder(self):
        # 아무것도 없는 트리를 조회할 때
        if self != None:
            print(self.value, end='') ###
            # 왼쪽 자식 있다면 왼쪽 자식 조회
            if self.left:
                self.left.preorder()
            # 오른쪽이 있다면 오른쪽 자식 조회
            if self.right:
                self.right.preorder()

    # 중위 순회 (좌부우)
    def preorder(self):
        # 아무것도 없는 트리를 조회할 때
        if self != None:

            # 왼쪽 자식 있다면 왼쪽 자식 조회
            if self.left:
                self.left.preorder()

            print(self.value, end='') ###

            # 오른쪽이 있다면 오른쪽 자식 조회
            if self.right:
                self.right.preorder()

    # 후위 순회 (좌우부)
    def preorder(self):
        # 아무것도 없는 트리를 조회할 때
        if self != None:

            # 왼쪽 자식 있다면 왼쪽 자식 조회
            if self.left:
                self.left.preorder()

            # 오른쪽이 있다면 오른쪽 자식 조회
            if self.right:
                self.right.preorder()

            print(self.value, end='') ###

arr = [1,2,1,3,2,4,3,5,3,6]
# 이진 트리 만들기 (인스턴스 생성)
nodes = [TreeNode(i) for i in range(0,14)]

for i in range(0, len(arr), 2):
    parentNode = arr[i]
    childNode = arr[i+1]
    nodes[parentNode].insert([nodes[childNode]])
