from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        if n!=m:
            return False
        sc = Counter(s)
        tc = Counter(t)
        for i, j in dict(sc).items():
            if tc[i] != j:
                return False
        return True
