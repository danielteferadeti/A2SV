class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        newList = []
        inner = []
        delCount = 0
        
        for i in range(len(strs[0])):
            for a in strs:
                inner.append(a[i])
            newList.append(inner)
            inner = []
        
        for col in newList:
            k = sorted(col)
            if k != col:
                delCount +=1
        return delCount