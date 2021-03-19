class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        preSum = 0
        prevSum = 0
        totalSum = 0
        
        for a in nums:
            totalSum += a
        
        for i in range(len(nums)):
            preSum = totalSum - nums[i] - prevSum
            
            if preSum == prevSum:
                return i
            prevSum += nums[i]
        
        return -1