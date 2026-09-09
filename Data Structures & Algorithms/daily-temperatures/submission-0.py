class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = []

        for i in range(0,len(temperatures)):
            currTemp = temperatures[i]
            daysAway = 0
            for j in range(i,len(temperatures)):
                if temperatures[j] > currTemp:
                    daysAway = j - i
                    break;
            res.append(daysAway)
        return res
