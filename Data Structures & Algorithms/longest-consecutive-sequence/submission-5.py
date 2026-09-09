class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seen = set(nums)
        longest_Seq = 0
        for i in range(len(nums)):
            num = nums[i]
            if (num - 1) not in seen:
                curr_Seq = 1
                while (num + curr_Seq)in seen:
                    curr_Seq +=1
                longest_Seq = max(curr_Seq,longest_Seq)
        return longest_Seq