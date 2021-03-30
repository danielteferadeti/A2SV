class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        leader = [x for x in range(1,len(edges)+1)]
        # print(leader)
        for_rank = dict()
        for x in leader:
            for_rank[x] = 1
        # print(leader)
        # print(for_rank)
        def find(a):
            c = a -1
            if a == leader[c]:
                return a
            leader[c] = find(leader[c])
            return leader[c]

        def union(a,b):
            a_lead = find(a)
            b_lead = find(b)
            if for_rank[a_lead] < for_rank[b_lead]:
                for_rank[b_lead] += for_rank[a_lead]
                leader[a_lead -1] = b_lead
            else:
                for_rank[a_lead] += for_rank[b_lead]
                leader[b_lead -1] = a_lead
        
        def connected(a: int, b: int):
            return find(a) == find(b)
        
        for cons in edges:
            if not connected(cons[0],cons[1]):
                union(cons[0],cons[1])
            else:
                return cons