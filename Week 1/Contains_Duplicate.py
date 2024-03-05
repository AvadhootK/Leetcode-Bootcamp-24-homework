class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # brute force - O(n**2)

        # sort - O(nlogn)
        # nums.sort()
        # for i in range(len(nums)-1):
        #     if nums[i]==nums[i+1]:
        #         return True
        # return False

        # set - O(n)
        s = set() # O(1) 
        # define set as search operation in set is faster(due to hash) compared to list(O(n))
        for n in nums: 
            if n in s:
                return True
            s.add(n) #O(1)
        return False

        # O(n**2) - create set from list
        # s = set(nums)
        # if len(s)<len(nums):
        #     return True
        # else:
        #     return False