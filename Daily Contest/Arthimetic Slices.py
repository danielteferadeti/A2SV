import sys
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        subarray = []
        diff = sys.maxsize
        
        if(len(nums) < 3):
            return 0
        for slow in range(len(nums)):
            inner = []
            inner.append(nums[slow])
            diff = sys.maxsize
            for fast in range(slow+1, len(nums)):
                if diff == sys.maxsize:
                    inner.append(nums[fast])
                    diff = nums[fast] - nums[slow]
                    continue
                if nums[fast] - nums[fast-1] == diff:
                    inner.append(nums[fast])
                else:
                    break
                if len(inner)>= 3:
                    subarray.append(inner)
                    
        return len(subarray)