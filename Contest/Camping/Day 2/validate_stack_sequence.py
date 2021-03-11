def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if len(pushed) == 0 or len(popped) == 0:
            return True
        startIndex = pushed.index(popped[0])
        stack = []
        
        for i in range(startIndex+1):
            stack.append(pushed[i])
            
        for i in range(len(popped)):
            if popped[i] not in  stack:
                if popped[i] != pushed[startIndex]:
                    return False
                stack.append(popped[i])
            if popped[i] == stack[-1]:
                stack.pop()
                startIndex += 1
            else:
                return False
            
        return True