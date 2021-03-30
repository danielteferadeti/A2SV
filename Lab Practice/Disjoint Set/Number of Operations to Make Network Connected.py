class Solution:
    def dfs(self, adjList: List[List[int]], visited: set, i: int):
        if i not in visited:
            visited.add(i)
            for a in adjList[i]:
                self.dfs(adjList,visited,a)
    

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        if len(connections) < n-1:
            return -1
        
        adjList = [[] for i in range(n)]
        for con in connections:
            adjList[con[0]].append(con[1])
            adjList[con[1]].append(con[0])
        print(adjList)
        
        Gr_comp = 0
        visited = set()
        for i in range(n):
            if i not in visited:
                Gr_comp +=1
                self.dfs(adjList,visited,i)
        return Gr_comp -1