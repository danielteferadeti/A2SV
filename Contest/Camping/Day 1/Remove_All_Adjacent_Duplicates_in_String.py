class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if len(s)==0:
            return ""
        stack = []
        result = ""
        
        for cur in s:
            if len(stack)==0:
                stack.append((cur, 1))
            else:
                prevCur, num = stack[-1]
                if prevCur == cur:
                    stack.pop()
                    stack.append((prevCur, num+1))
                    prevCur, num = stack[-1]
                else:
                    stack.append((cur, 1))
                if num == k:
                    stack.pop(-1)
        while stack:
            chur, num = stack.pop(0)
            result += str(chur)*num
        return result