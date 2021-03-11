class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        if tokens==[]:
            return 0
        score=0
        tokens.sort()
        if tokens[0]>P:
            return 0
        else:
            while len(tokens) > 0:
                if tokens[0] <= P:
                    score +=1
                    P -= tokens.pop(0)
                if len(tokens) > 1 and tokens[0] > P and score >0:
                    P += tokens.pop(-1)
                    score -=1
                if len(tokens) == 1 and P < tokens[0]:
                    return score
        return score

