class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        leader = [x for x in range(26)]
        for_rank = dict()
        for x in leader:
            for_rank[x] = 1
        # print(leader)
        def find(a):
            if a == leader[a]:
                return a
            leader[a] = find(leader[a])
            return leader[a]

        def union(a,b):
            a_lead = find(a)
            b_lead = find(b)
            if for_rank[a_lead] < for_rank[b_lead]:
                for_rank[b_lead] += for_rank[a_lead]
                leader[a_lead] = b_lead
            else:
                for_rank[a_lead] += for_rank[b_lead]
                leader[b_lead] = a_lead

        for equation in equations:
            x, y = equation[0], equation[-1]
            x, y= ord(x) - ord('a') , ord(y) - ord('a')
            if equation[1] == '=':
                union(x,y)

        for equation in equations:
            x, y = equation[0], equation[-1]
            x, y= ord(x) - ord('a') , ord(y) - ord('a')
            if equation[1] == '!' and find(x) == find(y):
                #print(for_rank)
                return False
        # print(leader)
        return True