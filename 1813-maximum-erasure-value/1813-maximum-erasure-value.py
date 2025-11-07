class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        dict = {}
        curr_sum = max_sum = 0
        start = 0

        for i,num in enumerate(nums):
            
            if num in dict and i >= start:
                while start <= dict[num]:
                    curr_sum -= nums[start]
                    start += 1
            dict[num] = i
            curr_sum += num
            max_sum = max(max_sum,curr_sum)
                
    
        return max_sum