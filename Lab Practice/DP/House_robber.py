class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = dict()
        memo[-2] = 0
        memo[-1] = 0
        
        for i in range(len(nums)):
            cur = nums[i]
            prev = memo[i -1]
            memo[i] = max(prev, cur + memo[i-2])
        return memo[len(nums) - 1]