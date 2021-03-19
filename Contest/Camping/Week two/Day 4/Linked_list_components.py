class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        connected = []
        soFar = []
        
        given =  set()
        for a in G:
            given.add(a)
    
        cur = head
        while cur!= None:
            if cur.val in given:
                soFar.append(cur.val)
            else:
                if len(soFar) !=0:
                    connected.append(soFar)
                    soFar = []
            cur = cur.next
        if len(soFar) != 0:
            connected.append(soFar)
            soFar = []
        return len(connected)
