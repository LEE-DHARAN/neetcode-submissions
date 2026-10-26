class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter

        n = len(nums)
        return [num for num, count in Counter(nums).items()
                if count > n // 3]
        