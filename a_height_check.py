"""
이 과제는 AI 사용이 불가합니다.
학생들이 서 있는 키 배열 heights가 주어질 때,
heights를 정렬한 expected 배열과 비교하여 위치가 다른 횟수를 반환하는 함수를 작성하세요.
"""

from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        """현재 학생 배열 heights와 정렬된 expected 배열을 비교하여 위치가 다른 횟수를 반환합니다.

        Args:
            heights: 현재 학생들이 서 있는 순서대로의 키 배열

        Returns:
            expected로 정렬했을 때 heights와 다른 인덱스의 개수
        """
        # 여기서부터 코드를 수정하세요
        return 0
        # 여기까지 코드를 수정하세요


def run_tests() -> None:
    solution = Solution()

    # 예제 1
    heights = [1, 1, 4, 2, 1, 3]
    res1 = solution.heightChecker(heights)
    assert res1 == 3, f"예제 1 실패: 기대 3, 실제 {res1}"
    print("예제 1: OK")


    # 예제 2
    heights = [5, 1, 2, 3, 4]
    res2 = solution.heightChecker(heights)
    assert res2 == 5, f"예제 2 실패: 기대 5, 실제 {res2}"
    print("예제 2: OK")


    # 예제 3
    heights = [1, 2, 3, 4, 5]
    res3 = solution.heightChecker(heights)
    assert res3 == 0, f"예제 3 실패: 기대 0, 실제 {res3}"
    print("예제 3: OK")


    # 추가 테스트: 중복 키 값
    heights = [2, 1, 2, 1, 2]
    res4 = solution.heightChecker(heights)
    assert res4 == 2, f"추가 테스트 실패: 기대 2, 실제 {res4}"
    print("추가 테스트: OK")


if __name__ == "__main__":
    run_tests()
        