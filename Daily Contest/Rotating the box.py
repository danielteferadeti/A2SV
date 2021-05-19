class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        
        for k in range(len(box)):
            ptr1, ptr2 = 0, 0
            while ptr2 != len(box[k]):
                if box[k][ptr2] == "#":
                    ptr2 +=1
                elif box[k][ptr2] == "*":
                    ptr2 +=1
                    ptr1= ptr2
                elif box[k][ptr2] == ".":
                    if ptr1 == ptr2:
                        ptr2+=1
                        ptr1=ptr2
                        continue
                    if ptr2==0:
                        ptr2 +=1
                        ptr1= ptr2
                        continue
                    if ptr2 == len(box[k])-1:
                        box[k] = box[k][0:ptr1]+[box[k][ptr2]]+box[k][ptr1:ptr2]
                        continue
                    if ptr1 ==0:
                        box[k] = [box[k][ptr2]] + box[k][ptr1:ptr2]+ box[k][ptr2+1:len(box[k])]
                        ptr2 +=1
                        ptr1 +=1
                        continue
                    box[k] = box[k][0:ptr1]+[box[k][ptr2]] + box[k][ptr1:ptr2]+ box[k][ptr2+1:len(box[k])]
                    ptr2 +=1
                    ptr1 +=1

        res = [["" for j in range(len(box))] for i in range(len(box[0]))]
        idx = len(box)-1
        for i in range(len(box)):
            for j in range(len(box[0])):
                res[j][idx-i] = box[i][j]
        return res