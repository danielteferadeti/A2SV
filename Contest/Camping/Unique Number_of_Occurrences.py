class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        visited = []
        occCount = []
        counter = 0
        for i in range(len(arr)):
            if arr[i] not in visited:
                visited.append(arr[i])
                for j in range(len(arr)):
                    if arr[i] == arr[j]:
                        counter +=1
                if counter not in occCount and counter != 0:
                    occCount.append(counter)
                    print(str(occCount))
                    counter = 0
                else:
                    return False
        return True