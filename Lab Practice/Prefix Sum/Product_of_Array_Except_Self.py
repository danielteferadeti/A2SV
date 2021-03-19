class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        pr_1 = []
        pr_1.append(1)
        pr_2 = []
        pr_2.append(1)
        
        for i in range(len(nums)):
            pr_1.append(pr_1[i]*nums[i])
        j = len(nums) -1
        while j > -1:
            pr_2.append(pr_2[len(nums) - (j+1)] * nums[j])
            j -= 1
        pr_2.reverse()
        
        for i in range(len(nums)):
            ans.append(pr_1[i]*pr_2[i+1])
        
        return ans