class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        givenList = A
        Totalmove = 0
        prev = -1
        
        givenList.sort()
        if(len(givenList) == 1):
            return 0
        for i in range(len(givenList)):
            cur = givenList[i]
            move = 0
            if cur <= prev:
                dif = prev - cur
                move = dif + 1
                Totalmove += move
                prev = cur + move
            else:
                prev = cur
        return Totalmove
