class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)

        while left < right:
            mid = (left + right) // 2
            needed_days = 1
            current = 0

            for weight in weights:
                if current + weight > mid:
                    needed_days += 1
                    current = 0
                current += weight

            if needed_days <= days:
                right = mid
            else:
                left = mid + 1

        return left