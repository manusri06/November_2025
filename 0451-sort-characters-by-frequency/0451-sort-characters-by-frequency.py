class Solution:
    def frequencySort(self, s: str) -> str:
        n = len(s)
        freq = {}
        for i in s:
            if i not in freq:
                freq[i] = 0
            freq[i]+=1

        bucket = [[] for _ in range(n+1)]

        for ch,count in freq.items():
            bucket[count].append(ch)

        s = []
        
        for i in range(n,0,-1):
            for j in bucket[i]:
                s.append(j*i)
        return "".join(s)
