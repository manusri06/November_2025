class Solution:
    def compress(self, chars: List[str]) -> int:

        start = 0         
        i = 0             
        n = len(chars)

        while i < n:
            j = i
           
            while j < n and chars[j] == chars[i]:
                j += 1
            
            count = j - i
            chars[start] = chars[i]
            start += 1

           
            if count > 1:
                for digit in str(count):
                    chars[start] = digit
                    start += 1
            i = j

        return start


 