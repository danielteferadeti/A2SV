class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1)== 0 or len(nums2)==0:
            return []
        interSec = []
        lenNum1 = len(nums1)
        lenNum2 = len(nums2)
        
        if lenNum1 <= lenNum2:
            for a in nums1:
                if a in nums2 and a not in interSec:
                    interSec.append(a)
        else:
            for a in nums2:
                if a in nums1 and a not in interSec:
                    interSec.append(a)
                    
        return interSec