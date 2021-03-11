class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if not len(pushed) and not len(popped):
            return False
        startIndex = pushed.index(popped[0])
        stack = []
        
        for i in range(startIndex+1):
            stack.append(pushed[i])
        for i in range(len(popped)):
            if popped[i] not in  stack:
                print("Not in Stack")
                stack.append(popped[i])
            if popped[i] == stack[-1]:
                stack.pop()
                #same how removed the popped last element too
            else:
                return False
        return True