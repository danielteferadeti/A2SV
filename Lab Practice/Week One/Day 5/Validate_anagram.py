class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        k = dict()
        for a in s:
            if a not in k:
                k[a] = 1
            else:
                k[a] = k[a] +1
        for b in t:
            if b not in k.keys():
                return False
            else:
                k[b] = k[b] - 1
                if k[b] <=0:
                    k.pop(b)
        if len(k)==0:
            return True