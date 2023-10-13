# Problem Link: https://leetcode.com/problems/contains-duplicate/

# Here is the optimal Solution as Discussed during the session.
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return True
        return False

# Here is the Bruteforce Solution as Discussed during the session.
# Note that it doesn't even pass all the testcases, and results in a Time Limit Exceeded Error!
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j and nums[i]==nums[j]:
                    return True
        return False
