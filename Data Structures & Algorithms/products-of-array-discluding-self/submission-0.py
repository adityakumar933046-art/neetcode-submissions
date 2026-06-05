class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = [1]*len(nums)
        b =1
        for i in range(len(nums)):
            a[i]= b
            b*=nums[i]
        c =1
        for i in range(len(nums)-1,-1,-1):
            a[i]*= c
            c*=nums[i]
        return a




        