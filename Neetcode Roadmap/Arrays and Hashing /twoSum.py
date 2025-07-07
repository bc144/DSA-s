'''

Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:

Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:

Input: nums = [4,5,6], target = 10

Output: [0,2]
Example 3:

Input: nums = [5,5], target = 10

Output: [0,1]
Constraints:

2 <= nums.length <= 1000
-10,000,000 <= nums[i] <= 10,000,000
-10,000,000 <= target <= 10,000,000



'''


#Brute Force solution 

from typing import List

class BruteForce:
    def twoSum(self,nums:List[int],target:int)->List[int]:
        for i in range(len(nums)): #Iterate over each element in the list 
            for j in range(i+1,len(nums)): #Iterate over the list again, with a +1 to the index to avoid self comparisons with the current index  
               if nums[i] + nums[j] == target: # If there are two values in the list that give the target result, return a list with the index of the values
                   return [i,j]
        return []
    




    # Entry point for running test cases
if __name__ == "__main__":
    solution = BruteForce()

    # Test cases: each is (input_list, target, expected_output)
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([1, 2, 3, 4, 5], 9, [3, 4]),
        ([0, 4, 3, 0], 0, [0, 3]),
        ([-3, 4, 3, 90], 0, [0, 2])
    ]

    # Running and printing results
    for i, (nums, target, expected) in enumerate(test_cases):
        result = solution.twoSum(nums, target)
        is_correct = result == expected or result == expected[::-1]  # Accept reverse order
        print(f"Test Case {i + 1}: nums={nums}, target={target} | Expected: {expected} | Result: {result} | {'✅' if is_correct else '❌'}")
