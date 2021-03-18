class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        k = dict()
        words = []
        paragraph = paragraph.lower()
        tempWord = ""
        
        for  char in paragraph:
            if ord(char) > 96 and ord(char) < 123:
                tempWord += char
            elif tempWord != "":
                words.append(tempWord)
                tempWord = ""
        if tempWord != "":
            words.append(tempWord)
            tempWord = ""
            
        for i in range(len(words)):
            word = words[i]
            if word in k:
                k[word] += 1
            else:
                k[word] = 1
        
        maxOcc, maxNum = "", -1
        for item in k.items():
            word, num = item
            if word not in banned:
                if num > maxNum:
                    maxOcc, maxNum = word, num
        return maxOcc