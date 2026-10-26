class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()

        # Find peak
        left, right = 0, n - 1

        while left < right:
            mid = (left + right) // 2

            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                left = mid + 1
            else:
                right = mid

        peak = left

        # Search ascending side
        left, right = 0, peak

        while left <= right:
            mid = (left + right) // 2
            value = mountain_arr.get(mid)

            if value == target:
                return mid
            elif value < target:
                left = mid + 1
            else:
                right = mid - 1

        # Search descending side
        left, right = peak + 1, n - 1

        while left <= right:
            mid = (left + right) // 2
            value = mountain_arr.get(mid)

            if value == target:
                return mid
            elif value > target:
                left = mid + 1
            else:
                right = mid - 1

        return -1