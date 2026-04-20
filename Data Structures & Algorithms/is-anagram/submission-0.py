class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        hash_map = {}
        for char in s:
            hash_map[char]=hash_map.get(char,0) + 1

        for char in t:
             if char not in hash_map or hash_map[char] == 0:
                return False
             hash_map[char] -= 1
        return True
        