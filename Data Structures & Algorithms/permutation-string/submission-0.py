class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter

        k = len(s1)
        target = Counter(s1)
        window = Counter(s2[:k])

        if window == target:
            return True

        for i in range(k, len(s2)):
            window[s2[i]] += 1
            window[s2[i-k]] -= 1

            if window[s2[i-k]] == 0:
                del window[s2[i-k]]

            if window == target:
                return True

        return False
        