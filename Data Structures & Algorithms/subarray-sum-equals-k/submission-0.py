class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = {0: 1}
        prefix = 0
        result = 0

        for num in nums:
            prefix += num
            result += counts.get(prefix - k, 0)
            counts[prefix] = counts.get(prefix, 0) + 1

        return result
        