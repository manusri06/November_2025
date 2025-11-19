class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        for ch in s:
            if ch not in freq:
                freq[ch] = 0
            freq[ch]+=1
        for i,j in enumerate(s):
            if freq[j] == 1:
                return i

        return -1