class Solution: 
    
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        result = ""
        
        shifts.reverse()
        
        sumRis = []
        Sum = 0
        for i in range(len(shifts)):
            Sum += shifts[i]
            sumRis.append(Sum)
        sumRis.reverse()
        
        for index in range(len(S)):
            newCharOrd = ord(S[index]) + (sumRis[index] % 26)
            if newCharOrd > 122:
                newCharOrd %= 122
                
            if newCharOrd < 97:
                newCharOrd += 96
                
            result += chr(newCharOrd)
           
        return  result