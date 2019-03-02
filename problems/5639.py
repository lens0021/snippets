# https://www.acmicpc.net/problem/5639
import sys
sys.setrecursionlimit(150000)

# 여러가지 방법을 시도해보는데 각 방법은 convert\d+라는 이름의 함수로 나타내어 있으며,
# 마지막 convert 함수를 제외하곤 일부 경우에서 실패합니다.


def convert1(lst):
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def postorder(node: Node):
        if node == None:
            return
        postorder(node.left)
        postorder(node.right)
        print(node.value)

    # Insert numbers to tree
    root = Node(lst[0])
    parent, node = None, None
    for num in lst[1:]:
        parent = None
        node = root
        while node != None:
            parent = node
            if num < node.value:
                node = node.left
            else:
                node = node.right

        new_node = Node(num)
        if num > parent.value:
            parent.right = new_node
        else:
            parent.left = new_node

    # Do traversal
    postorder(root)


def convert2(lst, low, high):
    '''이건 직접 생각해서 짠 구린 코드'''
    if low > high:
        return
    parent = lst[low]

    if low + 1 <= high:
        larger = None
        for i in range(low + 1, high + 1):
            if nums[i] > parent:
                larger = i
                break

        if larger == None:
            convert2(lst, low+1, high)
        else:
            convert2(lst, low+1, larger-1)
            convert2(lst, larger, high)
    print(parent)


def convert3(lst, minval, maxval):
    '''
    아래 코드에서 살짝 변형
    https://www.geeksforgeeks.org/find-postorder-traversal-of-bst-from-preorder-traversal/
    '''
    if convert3.index == len(lst):
        return

    if not (minval < lst[convert3.index] < maxval):
        return

    val = lst[convert3.index]
    convert3.index += 1

    convert3(lst, minval, val)
    convert3(lst, val, maxval)
    print(val)


convert3.index = 0

"""
문제에서 제시된 샘플:
              50
            /    \
         30       98
        /  \     /
      24    45 52
     /  \        \
    5    28       60

    Preorder : 50 30 24 5 28 45 98 52 60
    Postorder: 5 28 24 45 30 60 52 98 50

간단한 예제:
    1
     \
      2

    Preorder : 1 2
    Postorder: 2 1

    스택을 이용해 전위순회를 후위순회로 바꾸는 과정:
        스택에는 그 자체는 방문되었지만 서브트리는 아직 완전시 순회되지 않은 노드가 들어간다.
        Input: 1
        스택이 비었으므로 바로 추가한다.
            Stack: [1]
        Input: 2
        2는 1보다 크므로 1의 왼쪽 서브트리가 아니다. 즉 1의 왼쪽 서브트리에 대한 처리는 모두 끝났다.
        2는 1보다 크므로 1의 오른쪽 서브트리 혹은 1의 조상 중 하나의 오른쪽 서브트리이다.
         => 1에게는 조상이 없으므로 2는 1의 오른쪽 서브트리다
        2를 스택에 추가한다.
            Stack: [1, 2]
        Input: None
        스택을 비우며 출력한다.

간단한 예제:
        5
       /
      3
     /
    1

    Preorder : 5 3 1
    Postorder: 1 3 5

간단한 예제:
        5
       /
      3
     /
    1
     \
      2

    Preorder : 5 3 1 2
    Postorder: 2 1 3 5

간단한 예제:
    1
     \
      2
       \
        3
         \
          4

    Preorder : 1 2 3 4
    Postorder: 4 3 2 1

    스택을 이용해 전위순회를 후위순회로 바꾸는 과정:
        Input: 1
        스택이 비었으므로 바로 추가한다.
            Stack: [1]
        Input: 2
        2는 1보다 크므로 1의 왼쪽 서브 트리가 아니다. 즉 1의 왼쪽 서브 트리에 대한 처리는 모두 끝났다.
        2는 1보다 크므로 1의 오른쪽 서브트리 혹은 1의 조상 중 하나의 오른쪽 서브트리이다.
         => 1에게는 조상이 없으므로 2는 1의 오른쪽 서브트리다
        2를 스택에 추가한다.
            Stack: [1, 2]
        Input: 3
        3은 2보다 크므로 2의 왼쪽 서브 트리가 아니다. 즉 2의 왼쪽 서브 트리에 대한 처리는 모두 끝났다.
        3은 2보다 크므로 3의 오른쪽 서브트리 혹은 2의 조상 중 하나의 오른쪽 서브트리이다.
         => 스택[-2]가 스택[-1]보다 작으므로 3은 2의 조상의 서브트리는 아니며, 곧 3의 오른쪽 서브트리이다.
        3을 스택에 추가한다.
            Stack: [1, 2, 3]
        Input: 4
        의 왼쪽 서브 트리가 아니다. 즉 3의 왼쪽 서브 트리에 대한 처리는 모두 끝났다.
        4은 3보다 크므로 4의 오른쪽 서브트리 혹은 3의 조상 중 하나의 오른쪽 서브트리이다.
         => 스택[-2]가 스택[-1]보다 작으므로 4은 3의 조상의 서브트리는 아니며, 곧 3의 오른쪽 서브트리이다.
        4을 스택에 추가한다
            Stack: [1, 2, 3, 4]
        Input: None
        스택을 비우며 출력한다.

간단한 예제:
        5
       /
      3
     / \
    1   4

    Preorder : 5 3 1 4
    Postorder: 1 4 3 5

    스택을 이용해 전위순회를 후위순회로 바꾸는 과정:
        Input: 5
        스택이 비었으므로 바로 추가한다.
            Stack: [5]
        Input: 3
        3은 스택의 5보다 작으므로 5의 왼쪽 서브 트리이다.
        3을 스택에 추가한다.
            Stack: [5, 3]
        Input: 1
        1은 스택의 3보다 작으므로 3의 왼쪽 서브 트리이다.
        1을 스택에 추가한다.
            Stack: [5, 3, 1]
        Input: 4
        4는 1보다 크므로 1의 왼쪽 서브 트리가 아니다. 즉 1의 왼쪽 서브 트리에 대한 처리는 모두 끝났다.
        4는 1의 부모인 3보다도 크므로 1의 오른쪽 서브 트리도 아니다. 즉 1의 오른쪽 서브 트리에 대한 처리는 모두 끝났다.
        1의 서브 트리에 대한 처리가 모두 끝났으므로 1을 출력하고 스택에서 제거한다.
            Stack: [5, 3]
        4는 3보다 크므로 3의 왼쪽 서브 트리가 아니다. 즉 3의 왼쪽 서브 트리에 대한 처리는 모두 끝났다.
        4는 3의 부모인 5보다 작으므로 3의 오른쪽 서브 트리다.
        4를 스택에 추가한다.
            Stack: [5, 3, 4]
        Input: None
        스택을 비우며 출력한다.

"""


def convert4(lst):
    '''
    TODO
    재귀 없이 반복문만을 사용하는 함수
    '''

    if len(lst) == 1:
        print(lst[0])
    elif len(lst) == 0:
        return

    stack = []
    i = 0
    while i < len(lst):
        if not stack:
            stack.append(lst[i])
        else:
            new_number_is_left_subtree_of_last = lst[i] < stack[-1]
            new_number_is_right_subtree_of_last = (
                not new_number_is_left_subtree_of_last
                and (
                    len(stack) == 1
                    or
                    (len(stack) > 1 and stack[-2] < stack[-1])
                )
            )
            if new_number_is_left_subtree_of_last:
                stack.append(lst[i])
            elif new_number_is_right_subtree_of_last:
                stack.append(lst[i])
            else:
                print(stack.pop())
                continue

        i += 1

    while stack:
        print(stack.pop())


# Get input numbers
nums = []
try:
    while(True):
        nums.append(int(input()))
except EOFError:
    pass

# convert1(nums)
# convert2(nums, 0, len(nums)-1)
convert3(nums, 0, 1000000)
# convert4(nums)
