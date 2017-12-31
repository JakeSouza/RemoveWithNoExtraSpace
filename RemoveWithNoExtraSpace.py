'''
Created on Dec 30, 2017

@author: Jake
'''
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        #record size of array and create a pointer to look through array
        size = len(nums)
        count = len(nums)
        pointer = 0
        #for each slot in array
        for x in range(count):
            #if the pointer number and val are equal remove it and set pointer to look at same slot again
            if(nums[pointer] == val):
                nums.remove(val)
                size -= 1
                pointer -= 1
            #increment pointer to look at next spot
            pointer += 1
                
        return size