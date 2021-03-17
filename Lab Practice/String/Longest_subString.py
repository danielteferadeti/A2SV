class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j = 0,0
        mySet = set()
        maxLen = 0
        
        while j < len(s):
            char = s[j]
            if char not in mySet:
                mySet.add(char)
                j+=1
            else:
                mySet.remove(s[i])
                i+=1
            
            if len(mySet) > maxLen:
                maxLen = len(mySet)
        return maxLen