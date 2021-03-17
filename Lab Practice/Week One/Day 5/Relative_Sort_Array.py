class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        holder = dict()
        newArr = []
        
        for a in arr1:
            if a not in holder.keys():
                holder[a] = 1
            else:
                holder[a] = holder[a] + 1
        for b in arr2:
            for i in range(holder[b]):
                newArr.append(b)
            holder.pop(b)
        
        itemsLeft = sorted(holder.items())
        for c in itemsLeft:
            num, times = c
            for j in range(times):
                newArr.append(num)
                
        return newArr