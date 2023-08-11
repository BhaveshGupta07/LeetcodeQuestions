class Solution(object):
    def containsDuplicate(self, nums):
        nums.sort()
        l=len(nums)
        for i in range(1,l):
            if nums[i]==nums[i-1]:
                return True
            else:
                False

#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.