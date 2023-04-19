class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for idx in set(s):
            if s.count(idx) != t.count(idx):
                return False
        return True
        