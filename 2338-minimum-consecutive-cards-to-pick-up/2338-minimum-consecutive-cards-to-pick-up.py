class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        
        if len(cards) == len(set(cards)):
            return -1

        dict = {}
        start = 0
        minv = float('inf')
        for i,num in enumerate(cards):
            if num in dict:
                start = dict[num]
                minv = min(minv,i-start+1)
            dict[num] = i
        return minv



        