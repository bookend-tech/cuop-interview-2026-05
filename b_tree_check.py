"""
이 과제는 AI 사용이 불가합니다.
트리가 주어질 때, 각 레벨에서 가장 큰 값들을 반환하는 함수를 작성하세요.
예를 들어, 다음과 같은 트리가 주어질 때:
        1
       / \
      3   2
        / \   \
         5   3   9
각 레벨에서 가장 큰 값들은 [1, 3, 9]입니다.
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        """각 레벨에서 가장 큰 값들을 반환한다 (레벨 0부터)."""
        # 여기서부터 코드를 수정하세요
        return []
        # 여기까지 코드를 수정하세요


def build_tree_from_list(vals: List[Optional[int]]) -> Optional[TreeNode]:
    """레벨 순서 리스트에서 이진 트리를 생성한다. None은 null 노드를 의미."""
    if not vals:
        return None
    from collections import deque

    it = iter(vals)
    root_val = next(it)
    if root_val is None:
        return None
    root = TreeNode(root_val)
    q = deque([root])

    for v in it:
        node = q[0]
        if node.left is None:
            if v is not None:
                node.left = TreeNode(v)
                q.append(node.left)
            else:
                node.left = None
            continue

        if node.right is None:
            if v is not None:
                node.right = TreeNode(v)
                q.append(node.right)
            else:
                node.right = None
            q.popleft()

    return root


def _run_examples() -> None:
    sol = Solution()

    # Example 1
    tree1 = build_tree_from_list([1, 3, 2, 5, 3, None, 9])
    res1 = sol.largestValues(tree1)
    assert res1 == [1, 3, 9], f"Example 1 실패: 기대 [1, 3, 9], 실제 {res1}"
    print("Example 1: OK")

    # Example 2
    tree2 = build_tree_from_list([1, 2, 3])
    res2 = sol.largestValues(tree2)
    assert res2 == [1, 3], f"Example 2 실패: 기대 [1, 3], 실제 {res2}"
    print("Example 2: OK")

    # Example 3
    tree3 = build_tree_from_list([1, 2, 3, 4, 5])
    res3 = sol.largestValues(tree3)
    assert res3 == [1, 3, 5], f"Example 3 실패: 기대 [1, 3, 5], 실제 {res3}"
    print("Example 3: OK")

    # Example 4
    tree4 = build_tree_from_list([])
    res4 = sol.largestValues(tree4)
    assert res4 == [], f"Example 4 실패: 기대 [], 실제 {res4}"
    print("Example 4: OK")


if __name__ == "__main__":
    _run_examples()
