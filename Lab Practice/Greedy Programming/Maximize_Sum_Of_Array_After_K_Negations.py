class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        heapq.heapify(A)
        while K>0:
            cur = heapq.heappop(A)
            cur *=-1
            heapq.heappush(A,cur)
            K -=1
        return sum(A)