'''

Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false


'''

from typing import List

#Brute force solution , Time complexity O(n^2), Space Complexity: O(1)

class BruteForce:
    def hasDuplicate(self,nums:List[int])->bool:
        for i in range(len(nums)):  #Iterate over each element of the list
            for j in range (i+1,len(nums)): # Compare with every element ahead of it
                if nums[i] == nums[j]:  # Check for duplication
                    return True
    
        return False  #No duplicates
           
        
