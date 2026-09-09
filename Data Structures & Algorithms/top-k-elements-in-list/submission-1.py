from collections import defaultdict
class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       

        worst_Case = defaultdict(int)

        for num in nums:
            worst_Case[num] +=1

        items = list(worst_Case.items())
        items.sort(key = lambda x:x[1],reverse = True)
        res = []
        for i in range(k):
            res.append(items[i][0])
        return res