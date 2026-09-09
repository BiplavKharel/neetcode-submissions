import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        for i in range(len(stones)):
            stones[i] = -1 * stones[i]
        heapq.heapify(stones)
        print(stones)
        while len(stones) > 1:
            stone1 = -1 * heapq.heappop(stones)
            stone2 = -1 * heapq.heappop(stones)


            if stone1 > stone2:
                heapq.heappush(stones,(stone1 - stone2) * -1)
            
        res = stones[0] if stones else 0
        return (res * -1)