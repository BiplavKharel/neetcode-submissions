class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_zeros = 0
        zero_ind = -1
        res = [0] * len(nums)
        prod = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                nums_zeros+=1
                zero_ind = i
                if nums_zeros > 1:
                    return res
                continue
            prod *= nums[i]

        if nums_zeros == 1:
            res[zero_ind] = prod
            return res
        else: 
            for i,c in enumerate(nums):
                res[i] = prod//c
            return res
                
            




