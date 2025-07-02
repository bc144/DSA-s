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
    


           
        
# Entry point for running test cases
if __name__ == "__main__":
    solution1 = BruteForce()

    # Test cases
    test_cases = [
        ([1, 2, 3, 4], False),
        ([1, 2, 3, 1], True),
        ([99], False),
        ([1, 1, 1, 1], True),
        ([], False),
        ([3, 4, 5, 3, 2, 1], True)
    ]

    # Running and printing results
    for i, (input_list, expected) in enumerate(test_cases):
        result = solution1.hasDuplicate(input_list)
        print(f"Test Case {i + 1}: Input: {input_list} | Expected: {expected} | Result: {result} | {'✅' if result == expected else '❌'}")
