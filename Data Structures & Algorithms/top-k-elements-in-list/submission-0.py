class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Count the frequency of each element
        freqCount = {}
        freqList = [[] for i in range(len(nums) + 1)]
        for num in nums:
            freqCount[num] = 1 + freqCount.get(num, 0)
        
        for num,freq in freqCount.items():
           freqList[len(nums)-freq].append(num)
        
        ans = []
        
        for i in range(0,len(freqList)):
            for num in freqList[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans