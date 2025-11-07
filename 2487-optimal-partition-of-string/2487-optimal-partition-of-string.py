class Solution:
    def partitionString(self, s: str) -> int:

        if len(set(s)) == 1:
            return len(s)
        count = 1
        string = ""
        for i in s:
            if i in string:
                string = ""
                count += 1
            
            string+=i
        return count