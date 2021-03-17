class Solution:
    def removeDuplicates(self, S: str) -> str:
        queue = []
        for a in S:
            if len(queue) != 0:
                char = queue.pop(-1)
                if a == char:
                    pass
                else:
                    queue.append(char)
                    queue.append(a)
            else:
                queue.append(a)
        toReturn = ""
        while queue:
            char = queue.pop(0)
            toReturn += str(char)

        return toReturn