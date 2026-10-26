class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left, right = max(nums), sum(nums)

        while left < right:
            mid = (left + right) // 2
            parts = 1
            total = 0

            for num in nums:
                if total + num > mid:
                    parts += 1
                    total = 0
                total += num

            if parts <= k:
                right = mid
            else:
                left = mid + 1

        return left