class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        queue = []
        lastZeroindex = -1
        for i in range(len(seats)):
            cur = seats[i]
            if cur == 0:
                if i == lastZeroindex + 1 and len(queue)>0:
                    index, num, hasNext = queue.pop(-1)
                    num +=1
                    queue.append((index, num, hasNext))
                    lastZeroindex = i
                else:
                    queue.append((i,1,False))
                    lastZeroindex = i
            else:
                if len(queue)!=0:
                    index, num, hasNext = queue.pop(-1)
                    hasNext = True
                    queue.append((index, num, hasNext))
                    
        maxim = -1
        maxDis = 0
        checkNum = 0
        
        while queue:
            index, num, hasNext = queue.pop(0)
            checkNum = num
            maxFornow = 0
            if hasNext and index!=0:
                num = int(num/2)
            if num >= maxim:
                maxim = num
                if hasNext == False:
                    maxFornow = (index + num) - index
                else:
                    if(index == 0):
                        maxFornow = (index + num) - index
                    else:
                        if checkNum == 1:
                            maxFornow = int(index + checkNum) - index
                        elif(checkNum%2 == 0):
                            maxFornow = int(index + num) - index
                        else:
                            maxFornow = int(index + num ) - (index -1)
            if maxFornow > maxDis:
                maxDis = maxFornow
        
        return maxDis