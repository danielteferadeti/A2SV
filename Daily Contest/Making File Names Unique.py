class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        
        folders_so_far = set()
        k_checker = dict()
        ans = []
        
        for folder in names:
            if folder not in folders_so_far:
                folders_so_far.add(folder)
                k_checker[folder] = 0
                ans.append(folder)
            else:
                k = k_checker[folder]
                k +=1 
                temp = folder
                
                while True:
                    append = "(" + str(k) + ")"
                    folder += append
                    
                    if folder not in folders_so_far:
                        break
                    else:
                        k +=1
                        folder = temp
                
                folders_so_far.add(folder)
                k_checker[temp] = k
                k_checker[folder] = 0
                ans.append(folder)
                
        return ans