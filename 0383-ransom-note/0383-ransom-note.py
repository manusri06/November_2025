class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = [0]*26

        for i in magazine:
            freq[ord(i)-ord('a')] += 1

        for i in ransomNote:
            freq[ord(i)-ord('a')] -= 1
            if freq[ord(i)-ord('a')] < 0:
                return False
        return True