class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict = {}
        lmax = 0
        start = 0

        for i, ch in enumerate(s):
            if ch in dict and dict[ch] >= start:
                start = dict[ch]+1
            dict[ch] = i
            lmax = max(lmax, i-start+1)
        return lmax
